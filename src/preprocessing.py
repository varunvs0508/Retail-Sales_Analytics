import pandas as pd

def clean_data(df):
    df['order_date'] = pd.to_datetime(df['order_date'], format="mixed", dayfirst=True)

    df = df.dropna().drop_duplicates()

    df = df[(df['discount_pct'] >= 0) & (df['discount_pct'] <= 100)]
    df = df[df['quantity'] > 0]
    df = df[df['unit_price'] > 0]
    df = df[df['total_amount'] > 0]

    return df