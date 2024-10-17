from src.validation import Validation
from src.request import DukcapilPerson
from src.transformation import Transform
from src.conn_db import extract_data
from src.conn_db import load_data_to_postgres
from src.kafka import subscribe_to_kafka, produce_to_kafka, list_kafka_topics
import pandas as pd
import json


def enrich_data():
    print("Starting data enrichment...")
    # Validate Dukcapil Only when the NIK is not validate in table person
    df_person = extract_data('person')

    dukcapil = DukcapilPerson()

    # print(list_kafka_topics())

    # consume message from Kafka
    consumer = subscribe_to_kafka()

    print("Waiting for messages...")

    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None: continue

        data = json.loads(msg.value().decode('utf-8'))

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
                produce_to_kafka(data)
                # load_data_to_postgres(pd.DataFrame([data]), 'person')

if __name__ == "__main__":
        enrich_data()