# KafkaProducer

from kafka import KafkaProducer
import json
from time import sleep
import uuid
import os


DEFAULT_UUID = uuid.UUID(bytes=os.urandom(16), version=4)

# Cria uma instancia com o Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# formato json
jsonMessageToSend = {'uuid': str(DEFAULT_UUID),
                     'company_id': 1,
                     'country': 'Brazil'}

# producer.send - m�todo que grava na fila
producer.send('kafka-python-topic', value=jsonMessageToSend)

