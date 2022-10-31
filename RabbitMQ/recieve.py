AMQP_URL = "amqps://relnkbli:IvN1Fs_czxR2-zOw8qm3X0e8TCMjk5Jf@beaver.rmq.cloudamqp.com/relnkbli"
import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)