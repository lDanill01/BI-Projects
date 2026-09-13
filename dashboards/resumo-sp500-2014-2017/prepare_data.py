import json
from pathlib import Path
import numpy as np
import pandas as pd

root = Path(__file__).resolve().parents[2]
source = root / '.data' / 'S&P 500 Stock Prices 2014-2017.csv'
out = Path(__file__).parent / 'data.json'
script_out = Path(__file__).parent / 'data.js'
df = pd.read_csv(source, parse_dates=['date']).sort_values(['symbol', 'date'])
df['dailyReturn'] = df.groupby('symbol')['close'].pct_change()
stats = df.groupby('symbol').agg(first=('close','first'), last=('close','last'), observations=('close','count'), volatility=('dailyReturn','std'), volume=('volume','mean')).reset_index()
stats['return'] = stats['last'] / stats['first'] - 1
stats = stats.replace([np.inf, -np.inf], np.nan).fillna(0)
top = stats.sort_values('return', ascending=False).head(12)['symbol'].tolist()
bottom = stats.sort_values('return').head(8)['symbol'].tolist()
focus = list(dict.fromkeys(top + bottom + ['AAPL','MSFT','AMZN','GOOGL','SPY']))
series = {}
for symbol in focus:
    g = df[df.symbol == symbol][['date','close']].dropna()
    if g.empty:
        continue
    base = g.close.iloc[0]
    series[symbol] = [{'date': d.strftime('%Y-%m-%d'), 'value': round(float(v / base * 100), 3)} for d, v in zip(g.date, g.close)]
payload = {
    'meta': {'rows': int(len(df)), 'assets': int(df.symbol.nunique()), 'start': df.date.min().strftime('%Y-%m-%d'), 'end': df.date.max().strftime('%Y-%m-%d'), 'missing': int(df.isna().sum().sum())},
    'stats': [{'symbol': r['symbol'], 'return': round(float(r['return']), 6), 'volatility': round(float(r['volatility']), 6), 'observations': int(r['observations']), 'volume': round(float(r['volume']), 0)} for r in stats.to_dict('records')],
    'series': series,
    'market': [{'date': d.strftime('%Y-%m-%d'), 'value': round(float(v), 3)} for d, v in df.groupby('date').close.mean().items()]
}
out.write_text(json.dumps(payload, separators=(',', ':')), encoding='utf-8')
script_out.write_text('const DASHBOARD_DATA = ' + json.dumps(payload, separators=(',', ':')) + ';', encoding='utf-8')
print(f'Gerado: {out} ({len(payload["stats"])} ativos; {len(payload["market"])} datas)')
