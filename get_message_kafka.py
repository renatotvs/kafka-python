# KafkaConsumer

from kafka import KafkaConsumer
import json

# Cria uma instancia com o Kafka consumer
consumer = KafkaConsumer('kafka-python-topic', bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True, group_id='my-group',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# busca mensagens na fila
for message in consumer:
    print(message.value)

