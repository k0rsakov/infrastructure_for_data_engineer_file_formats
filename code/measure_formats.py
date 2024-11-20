import os

import pandas as pd


def measure_formats() -> pd.DataFrame:
    """
    Функция, которая позволяет посчитать объём файлов в разных форматах.

    :return: pd.DataFrame c данными.
    """

    results = []

    # Размеры файлов
    files = {
        "parquet": "../data/data.parquet",
        "csv": "../data/data.csv",
        "csv.gz": "../data/data.csv.gz",
        "json": "../data/data.json",
        # "avro": "../data/data.avro",
    }

    for format_name, filename in files.items():
        if os.path.exists(filename):
            size = os.path.getsize(filename)

            results.append({
                "format": format_name,
                "size_mb": size / (1024 * 1024),
            })

    return pd.DataFrame(results)


print(measure_formats())
