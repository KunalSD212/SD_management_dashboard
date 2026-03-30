import pandas as pd

def load_mis():
    df = pd.read_excel("data/mis_master.xlsx")

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    return df
