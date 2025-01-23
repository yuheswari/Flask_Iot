import pika
#uses amrp protocol to communicate with rabbitmq
credentials = pika.PlainCredentials('yuheswari', 'Asuk_2627')
parameters = pika.ConnectionParameters('rabbitmq.selfmade.ninja', 5672,'yuheswari2525_helloworld',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='my_first queue manu!!')
channel.basic_publish(exchange='',
                      routing_key='my_first queue manu!!',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()