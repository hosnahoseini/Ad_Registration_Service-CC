AMQP_URL = "amqps://relnkbli:IvN1Fs_czxR2-zOw8qm3X0e8TCMjk5Jf@beaver.rmq.cloudamqp.com/relnkbli"
import pika, sys, os

def send(msg):
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='advertisements')

    channel.basic_publish(exchange='', routing_key='advertisements', body=MsgFlag)
    print(f" [x] Sent {msg}")
    connection.close()

