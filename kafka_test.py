from kafka import KafkaConsumer

consumer = KafkaConsumer('exo1', bootstrap_servers=['51.38.185.58'])

for message in consumer:
    print(message.value.decode('utf-8'))

