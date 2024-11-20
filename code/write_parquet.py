from generate_data import generate_users

df = generate_users()

df.to_parquet(path="../data/data.parquet")
