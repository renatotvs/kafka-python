# README #

Neste arquivo Readme está documentado o que é necessário para instalar e procedimentos para comunicação com o Kafka.

### Instação da biblioteca Python

pip install kafka-python

### Kafka Producer

from kafka import KafkaProducer

### Kafka Consumer

from kafka import KafkaConsumer

### Send Message

producer = KafkaProducer('localhost:2181',
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

data = {'number': 1}

producer.send('topic_name', value=data)

### Load Message

consumer = KafkaConsumer('topic_name', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest',
                         enable_auto_commit=False, group_id='my-group',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))
                         
foreach message in consumer:
    print(message.value)