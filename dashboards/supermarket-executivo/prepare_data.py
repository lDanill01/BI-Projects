import json
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[2]
df = pd.read_csv(root / 'data/Datasets/Sales/supermarket_sales.csv', parse_dates=['Date'])
df['hour'] = pd.to_datetime(df['Time']).dt.hour
def rows(g):
    return {'compras': int(len(g)), 'receita': round(float(g.Total.sum()), 2), 'ticket': round(float(g.Total.mean()), 2), 'margem': round(float(g['gross income'].sum()), 2), 'avaliacao': round(float(g.Rating.mean()), 2), 'quantidade': round(float(g.Quantity.mean()), 2)}
payload = {'meta': {'compras': len(df), 'receita': round(float(df.Total.sum()),2), 'ticket': round(float(df.Total.mean()),2), 'margem': round(float(df['gross income'].sum()),2), 'avaliacao': round(float(df.Rating.mean()),2), 'margemPct': round(float(df['gross income'].sum()/df.Total.sum()*100),2), 'inicio': df.Date.min().strftime('%d/%m/%Y'), 'fim': df.Date.max().strftime('%d/%m/%Y')}, 'filiais': [], 'produtos': [], 'perfis': [], 'pagamentos': [], 'horas': []}
for (branch, city), g in df.groupby(['Branch','City']): payload['filiais'].append({'nome': branch, 'cidade': city, **rows(g)})
for name, g in df.groupby('Product line'): payload['produtos'].append({'nome': name, **rows(g)})
for name, g in df.groupby('Customer type'): payload['perfis'].append({'nome': name, **rows(g)})
for name, g in df.groupby('Payment'): payload['pagamentos'].append({'nome': name, **rows(g)})
for hour, g in df.groupby('hour'): payload['horas'].append({'hora': int(hour), **rows(g)})
Path(__file__).parent.mkdir(parents=True, exist_ok=True)
Path(__file__).parent.joinpath('data.js').write_text('const SALES_DATA = ' + json.dumps(payload, ensure_ascii=False, separators=(',', ':')) + ';', encoding='utf-8')
print('Dados gerados:', payload['meta'])
