from kafka import KafkaProducer
import time

bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
producer = KafkaProducer()

for message in range(0, 100):
    time.sleep(3)
    ack = producer.send(topicName, b'Hello World!!!!!!!!')
    metadata = ack.get()
    print(metadata.topic)
    print(metadata.partition)
