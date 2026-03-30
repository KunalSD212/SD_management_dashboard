import pandas as pd

def load_mis():
    df = pd.read_excel("data/mis_master.xlsx")

    # Clean column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Debug (very important for now)
    print("Columns in MIS:", df.columns)

    # Handle date/month column safely
    if "month" in df.columns:
        df["date"] = pd.to_datetime(df["month"], errors="coerce")
    elif "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    else:
        raise ValueError(f"No 'month' or 'date' column found. Available columns: {df.columns}")

    return df