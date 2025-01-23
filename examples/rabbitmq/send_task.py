#!/usr/bin/env python
import pika
import sys

# Update the connection parameters with the correct username and password
credentials = pika.PlainCredentials('yuheswari', 'Asuk_2627')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq.selfmade.ninja', virtual_host='yuheswari2525_helloworld', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2  # make message persistent
    ))
print(f" [x] Sent {message}")
connection.close()