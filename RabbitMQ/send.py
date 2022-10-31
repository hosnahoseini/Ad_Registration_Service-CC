AMQP_URL = "amqps://relnkbli:IvN1Fs_czxR2-zOw8qm3X0e8TCMjk5Jf@beaver.rmq.cloudamqp.com/relnkbli"
import pika

connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()