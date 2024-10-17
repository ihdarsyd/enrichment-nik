from confluent_kafka import Consumer, Producer, KafkaException
from confluent_kafka.admin import AdminClient  # Correct import for AdminClient
from dotenv import load_dotenv
import os
import json

load_dotenv(".env")
KAFKA_SERVER = os.getenv('KAFKA_SERVER')
KAFKA_GROUP = "training"
KAFKA_TOPIC = "dukcapil"
KAFKA_TOPIC_REPLY = "dukcapil.reply"

# Function to consume messages from Kafka
def subscribe_to_kafka():
    consumer = Consumer({
        'bootstrap.servers': KAFKA_SERVER,
        'group.id': KAFKA_GROUP,
        'auto.offset.reset': 'earliest'
    })

    consumer.subscribe([KAFKA_TOPIC])
    return consumer

# Function to produce messages to Kafka
def produce_to_kafka(message):
    try:
        producer = Producer({'bootstrap.servers': KAFKA_SERVER})
        producer.produce(KAFKA_TOPIC_REPLY, value=json.dumps(message).encode('utf-8'))
        producer.flush()  # Ensure all messages are sent
    except KafkaException as e:
        print(f"Error producing message: {e}")

def list_kafka_topics():
    # Create an admin client
    admin_client = AdminClient({'bootstrap.servers': KAFKA_SERVER})

    # Fetch the list of topics
    try:
        topics = admin_client.list_topics(timeout=10)  # 10 seconds timeout
        print("Kafka Topics: ", topics.topics)
        return topics.topics
    except KafkaException as e:
        print(f"Error listing topics: {e}")
        return []

