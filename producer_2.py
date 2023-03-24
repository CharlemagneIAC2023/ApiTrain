import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['51.38.185.58'])
topic = 'Charlemagne'

message = {"data": [[1, 2], [3, 4]]}
producer.send(topic, json.dumps(message).encode('utf-8'))

