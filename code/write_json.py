from generate_data import generate_users

df = generate_users()

df.to_json(path_or_buf="../data/data.json")
