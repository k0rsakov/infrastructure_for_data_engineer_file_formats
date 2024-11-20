import json

import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter
from generate_data import generate_users

df = generate_users(size_of_generate=1)


# Определение схемы
schema = {
    "type": "record",
    "name": "user",
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "created_at", "type": "string"},
        {"name": "updated_at", "type": "string"},
        {"name": "first_name", "type": "string"},
        {"name": "middle_name", "type": "string"},
        {"name": "birthday", "type": "string"},
        {"name": "email", "type": "string"},
        {"name": "city", "type": "string"},
    ],
}

# Преобразуем datetime колонки в строки
datetime_columns = ["created_at", "updated_at", "birthday"]
for col in datetime_columns:
    df[col] = df[col].astype(str)

# Запись в Avro
with DataFileWriter(
        open("../data/data.avro", "wb"),
        DatumWriter(),
        avro.schema.parse(json.dumps(schema)),
) as writer:
    for _, row in df[[
            "id",
            "created_at",
            "updated_at",
            "first_name",
            "last_name",
            "middle_name",
            "birthday",
            "email",
            "city"]].iterrows():
        writer.append({
            "id": row["id"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
            "first_name": row["first_name"],
            "middle_name": row["middle_name"],
            "birthday": row["birthday"],
            "email": row["email"],
            "city": row["city"],
        })

