import pika, sys, os

AMQP_URL = "amqps://relnkbli:IvN1Fs_czxR2-zOw8qm3X0e8TCMjk5Jf@beaver.rmq.cloudamqp.com/relnkbli"

def send(msg):
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='advertisements')

    channel.basic_publish(exchange='', routing_key='advertisements', body=msg)
    print(f" [x] Sent {msg}")
    connection.close()

if __name__ == '__main__':
    send("test")