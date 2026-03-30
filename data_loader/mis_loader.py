import pandas as pd

def load_mis():
    df = pd.read_excel("data/mis_master.xlsx")

    # Clean column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Handle month/date column
    if "month" in df.columns:
        df["date"] = pd.to_datetime(df["month"])
    elif "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
    else:
        raise ValueError("No 'month' or 'date' column found in MIS file")

    return df
