from avro.datafile import DataFileReader
from avro.io import DatumReader

with DataFileReader(
    open("../data/data.avro", "rb"),
    DatumReader(),
) as reader:
    for record in reader:
        print(record)
