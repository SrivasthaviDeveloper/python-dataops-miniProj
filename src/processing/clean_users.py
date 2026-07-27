import pandas as pd

df = pd.read_csv("data/raw/users.csv")

df = df.drop_duplicates()

df = df.dropna()

df.to_csv(
    "data/processed/users_clean.csv",
    index=False
)