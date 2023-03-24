from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['51.38.185.58'])
topic = 'exo1'

message = 'coucou Charlemagne'
producer.send(topic, message.encode('utf-8'))

