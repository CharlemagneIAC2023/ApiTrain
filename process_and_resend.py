import json
import numpy as np
from kafka import KafkaConsumer, KafkaProducer

bootstrap_servers = ['51.38.185.58']
topic_input = 'package.json'
topic_output = 'processed'

consumer = KafkaConsumer(topic_input, bootstrap_servers=bootstrap_servers, 
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

for message in consumer:
    data = np.array(message.value['data'])
    sum_data = np.sum(data)
    result = {'sum': sum_data}
    producer.send(topic_output, json.dumps(result).encode('utf-8'))

