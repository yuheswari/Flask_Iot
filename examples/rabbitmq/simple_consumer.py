import pika
#uses amrp protocol to communicate with rabbitmq

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

credentials = pika.PlainCredentials('yuheswari', 'Asuk_2627')
parameters = pika.ConnectionParameters('rabbitmq.selfmade.ninja', 5672,'yuheswari2525_helloworld',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='my_first queue manu!!')
channel.basic_consume(queue='my_first queue manu!!',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()