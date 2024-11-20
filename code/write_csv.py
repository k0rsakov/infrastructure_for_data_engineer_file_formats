from generate_data import generate_users

df = generate_users()

df.to_csv(path_or_buf='../data/data.csv')