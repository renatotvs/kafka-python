# Kafk com Python #

Comunicação com filas do Kafka em python.

### Instação da biblioteca do kafka

pip install kafka-python

### Send Message

from kafka import KafkaProducer

producer = KafkaProducer('localhost:2181',
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

### Load Message

from kafka import KafkaConsumer

consumer = KafkaConsumer('topic_name', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest',
                         enable_auto_commit=False, group_id='my-group',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))
                         