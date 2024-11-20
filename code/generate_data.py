import pandas as pd
import uuid

list_of_dict = []
for _ in range(1000000):
    dict_ = {
        "id": uuid.uuid4(),
        "created_at": fake.date_time_ad(
            start_datetime=datetime.date(year=2024, month=1, day=1),
            end_datetime=datetime.date(year=2025, month=1, day=1),
        ),
        "updated_at": fake.date_time_ad(
            start_datetime=datetime.date(year=2024, month=1, day=1),
            end_datetime=datetime.date(year=2025, month=1, day=1),
        ),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "middle_name": fake.middle_name(),
        "birthday": fake.date_time_ad(
            start_datetime=datetime.date(year=1980, month=1, day=1),
            end_datetime=datetime.date(year=2005, month=1, day=1),
        ),
        "email": fake.email(),
        "city": fake.city(),
    }

    list_of_dict.append(dict_)

df = pd.DataFrame(data=list_of_dict)