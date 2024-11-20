
import pandas as pd

df = pd.read_csv(
    filepath_or_buffer="../data/data.csv",
    parse_dates=["created_at"],
)

print(df.dtypes)
