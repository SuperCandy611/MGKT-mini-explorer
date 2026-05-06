import pandas as pd


def load_clean_data(path: str) -> pd.DataFrame:
    """Load MGKT CSV and remove implausible / unstated-gender rows.

    Filters applied:
        - age: 13 <= age <= 80
        - gender: != 0  (0 = unstated)

    Prints a cleaning summary to stdout.
    Returns the cleaned DataFrame.
    """
    df = pd.read_csv(path)
    n_raw = len(df)

    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["gender"] = pd.to_numeric(df["gender"], errors="coerce")

    df = df[(df["age"] >= 13) & (df["age"] <= 80)]
    df = df[df["gender"] != 0]
    df = df.dropna(subset=["age", "gender"])
    n_clean = len(df)

    pct_lost = (n_raw - n_clean) / n_raw * 100
    print(f"Raw rows loaded  : {n_raw:>7,}")
    print(f"Rows after filter: {n_clean:>7,}")
    print(f"Rows dropped     : {n_raw - n_clean:>7,}  ({pct_lost:.1f}%)")

    return df.reset_index(drop=True)
