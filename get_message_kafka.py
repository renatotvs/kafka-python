# KafkaConsumer

from kafka import KafkaConsumer
import json


consumer = KafkaConsumer('kafka-python-topic', bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True, group_id='my-group',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))


for message in consumer:
    print(message.value)

