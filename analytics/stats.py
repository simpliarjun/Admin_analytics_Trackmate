import pandas as pd

def most_travelled_destination(df: pd.DataFrame, top_n=10) -> pd.Series:
    return df["Destination"].value_counts().head(top_n)

def most_used_transport(df: pd.DataFrame) -> pd.Series:
    return df["Mode of Transport"].value_counts()

def most_used_fuel(df: pd.DataFrame) -> pd.Series:
    return df["Fuel Type"].value_counts()

def average_distance_monthly(df: pd.DataFrame) -> pd.Series:
    df["Month"] = df["Trip Start Date"].dt.to_period("M")
    return df.groupby("Month")["Distance (km)"].mean()

def most_common_purpose(df: pd.DataFrame) -> pd.Series:
    return df["Purpose"].value_counts()

def average_companions(df: pd.DataFrame) -> float:
    return float(df["Companions"].mean())

def average_spent(df: pd.DataFrame) -> float:
    return float(df["Total Cost (INR)"].mean())

def most_travelled_routes(df: pd.DataFrame, top_n=10) -> pd.Series:
    if "Most Travelled Route" in df.columns:
        return df["Most Travelled Route"].value_counts().head(top_n)
    df["Route"] = df["Origin"] + " - " + df["Destination"]
    return df["Route"].value_counts().head(top_n)

def co2_monthly(df: pd.DataFrame) -> pd.Series:
    df["Month"] = df["Trip Start Date"].dt.to_period("M")
    return df.groupby("Month")["Carbon Emission (kg)"].sum()

def average_toll(df: pd.DataFrame) -> float:
    return 0.0
