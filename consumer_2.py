import json
import numpy as np
from kafka import KafkaConsumer

consumer = KafkaConsumer('Charlemagne', bootstrap_servers=['51.38.185.58'], 
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    data = np.array(message.value['data'])
    sum_data = np.sum(data)
    print(f"La somme des valeurs du message reçu est {sum_data}")

