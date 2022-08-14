from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'on-demand-result',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='group-id-name',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print('Messsage: {}'.format(message))
