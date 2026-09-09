"""Gera o pacote local de dados agregados para o dashboard do Airbnb."""

import json
from pathlib import Path

import pandas as pd


DATASET = Path.home() / ".cache/kagglehub/datasets/arianazmoudeh/airbnbopendata/versions/1/Airbnb_Open_Data.csv"
OUTPUT = Path(__file__).parents[1] / "dashboards/airbnb-exploracao/data.js"


def clean_text(series):
    return series.fillna("Não informado").astype(str).str.strip().replace("", "Não informado")


def build_payload(df):
    df = df.copy()
    df["price_num"] = pd.to_numeric(
        df["price"].astype("string").str.replace(r"[$,]", "", regex=True), errors="coerce"
    )
    df["region"] = clean_text(df["neighbourhood group"]).str.title()
    df["roomType"] = clean_text(df["room type"])
    df["neighbourhoodClean"] = clean_text(df["neighbourhood"])
    df["availability_num"] = pd.to_numeric(df["availability 365"], errors="coerce")
    df["reviews_num"] = pd.to_numeric(df["number of reviews"], errors="coerce")
    df["reviewRate"] = pd.to_numeric(df["review rate number"], errors="coerce")

    valid_availability = df["availability_num"].between(0, 365)
    valid_price = df["price_num"].notna()

    def median(column):
        value = df[column].median()
        return round(float(value), 1) if pd.notna(value) else None

    summary = {
        "listings": int(len(df)),
        "priceMedian": median("price_num"),
        "priceMean": round(float(df["price_num"].mean()), 1),
        "reviewMedian": median("reviews_num"),
        "availabilityMean": round(float(df.loc[valid_availability, "availability_num"].mean()), 1),
        "priceP95": round(float(df["price_num"].quantile(0.95)), 1),
        "missingPricePct": round(float((~valid_price).mean() * 100), 1),
        "invalidAvailabilityPct": round(float((~valid_availability).mean() * 100), 1),
    }

    def grouped(group_columns, limit=None):
        result = (
            df.groupby(group_columns, dropna=False)
            .agg(
                listings=("id", "size"),
                priceMean=("price_num", "mean"),
                priceMedian=("price_num", "median"),
                availabilityMean=("availability_num", "mean"),
                availabilityMedian=("availability_num", "median"),
                reviewsMean=("reviews_num", "mean"),
                reviewsMedian=("reviews_num", "median"),
                ratingMedian=("reviewRate", "median"),
            )
            .reset_index()
            .sort_values("listings", ascending=False)
        )
        if limit:
            result = result.head(limit)
        return result

    def records(frame):
        output = []
        for row in frame.to_dict("records"):
            output.append({
                key: (None if pd.isna(value) else (float(value) if hasattr(value, "item") and isinstance(value.item(), float) else value.item() if hasattr(value, "item") else value))
                for key, value in row.items()
            })
        return output

    room = grouped(["roomType"])
    regions = grouped(["region"])
    neighbourhoods = grouped(["region", "neighbourhoodClean"], 30)
    matrix = grouped(["region", "roomType"])

    sample = df.loc[valid_price, ["id", "NAME", "region", "neighbourhoodClean", "roomType", "price_num", "availability_num", "reviews_num", "reviewRate"]].copy()
    sample = sample.sort_values("reviews_num", ascending=False)
    sample = sample.head(180).fillna(0)
    sample_records = []
    for row in sample.to_dict("records"):
        sample_records.append({
            "id": int(row["id"]),
            "name": str(row["NAME"])[:90] if row["NAME"] else "Sem nome",
            "region": str(row["region"]),
            "neighbourhood": str(row["neighbourhoodClean"]),
            "roomType": str(row["roomType"]),
            "price": round(float(row["price_num"]), 1),
            "availability": round(float(row["availability_num"]), 1),
            "reviews": round(float(row["reviews_num"]), 1),
            "rating": round(float(row["reviewRate"]), 1),
        })

    segment_frame = df.assign(
        priceBand=pd.cut(df["price_num"], [-float("inf"), 100, 200, 400, float("inf")], labels=["Até R$ 100", "R$ 101–200", "R$ 201–400", "Acima de R$ 400"]).astype("string").fillna("Não informado"),
        availabilityBand=pd.cut(df["availability_num"], [-float("inf"), 0, 30, 180, 365, float("inf")], labels=["0 dias", "1–30 dias", "31–180 dias", "181–365 dias", "Inválido/ausente"]).astype("string").fillna("Inválido/ausente"),
    )

    payload = {
        "meta": {"source": "Airbnb_Open_Data.csv", "rows": int(len(df)), "columns": 26, "note": "Diagnóstico de anúncios; não representa reservas, ocupação ou receita realizada."},
        "summary": summary,
        "roomTypes": records(room.rename(columns={"roomType": "label"})),
        "regions": records(regions.rename(columns={"region": "label"})),
        "neighbourhoods": records(neighbourhoods.rename(columns={"neighbourhoodClean": "label"})),
        "matrix": records(matrix),
        "segments": records(
            segment_frame
            .groupby(["region", "roomType", "priceBand", "availabilityBand"], dropna=False)
            .agg(listings=("id", "size"), priceMean=("price_num", "mean"), availabilityMean=("availability_num", "mean"), reviewsMean=("reviews_num", "mean"))
            .reset_index()
            .rename(columns={"priceBand": "priceBand", "availabilityBand": "availabilityBand"})
        ),
        "availabilityBands": [
            {"label": "0 dias", "listings": int((df["availability_num"] == 0).sum())},
            {"label": "1–30 dias", "listings": int(df["availability_num"].between(1, 30).sum())},
            {"label": "31–180 dias", "listings": int(df["availability_num"].between(31, 180).sum())},
            {"label": "181–365 dias", "listings": int(df["availability_num"].between(181, 365).sum())},
            {"label": "Inválido/ausente", "listings": int((~valid_availability).sum())},
        ],
        "sampleListings": sample_records,
    }
    return payload


def main():
    if not DATASET.exists():
        raise FileNotFoundError(f"Dataset não encontrado: {DATASET}")
    payload = build_payload(pd.read_csv(DATASET, low_memory=False))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("window.AIRBNB_DATA = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    print(f"Gerado {OUTPUT} com {payload['meta']['rows']:,} registros de origem e {len(payload['sampleListings'])} linhas de consulta.")


if __name__ == "__main__":
    main()
