import pandas as pd

df = pd.read_parquet(path="../data/data.parquet", columns=["id", "city"])

print(df)
