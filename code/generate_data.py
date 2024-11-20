import datetime
import uuid

import pandas as pd
from faker import Faker


def generate_users(size_of_generate: int = 1000000) -> pd.DataFrame:
    """
    Функция-генератор.

    Позволяет создать случайных пользователей для работы с ними.

    :param size_of_generate: Количество пользователей для генерации.
    :return: pd.DataFrame с данными.
    """
    fake = Faker(locale="ru_RU")

    list_of_dict = []

    for _ in range(size_of_generate):
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

    return pd.DataFrame(data=list_of_dict)
