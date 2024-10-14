from src.validation import Validation
from src.request import DukcapilPerson
from src.transformation import Transform
from src.conn_db import extract_data
from src.conn_db import load_data_to_postgres
import pandas as pd

# Validate Dukcapil Only when the NIK is not validate in table person
df_person = extract_data('person')

dukcapil = DukcapilPerson()

# read data from spppti.json
with open('spptti.json') as f:
    data = f.read()

validate = Validation(data)
nik = validate.validate_person()

# if nik is not in df_person
if nik not in df_person['nomor_identitas'].values and nik:
    dukcapil_data = dukcapil.search_nik(nik)
    if dukcapil_data.get('message') == 'Person not found':
        print('NIK not found in Dukcapil')
    else:
        transform = Transform(dukcapil_data)
        data = transform.transform_data()
        load_data_to_postgres(pd.DataFrame([data]), 'person')