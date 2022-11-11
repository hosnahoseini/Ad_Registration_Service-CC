import os
import sys
import functools
import asyncio
import pika
import requests

from src.api.immega import evaluate
from src.api.mailgun import send_simple_message
from src.api.s3 import get_url

AMQP_URL = "amqps://relnkbli:IvN1Fs_czxR2-zOw8qm3X0e8TCMjk5Jf@beaver.rmq.cloudamqp.com/relnkbli"

def main():
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='advertisements')
 

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        # recieve img from s3
        image = get_url(body)
        result = evaluate(image)
        
        if (result):
            state = "confirmed"
            category = "vehicle"
        else:
            state = "denied"
            category = "not vehicle"

        id = str(body).split(".")[0].split("'")[1]
        # put(id, state, category)
        requests.put(f'http://localhost:8000/update_advertisement/?id={id}&state={state}&category={category}')
        send_mail(id, result)

    channel.basic_consume(queue='advertisements', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()    

def sync(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))
    return wrapper


def send_mail(id, result):
    response = requests.get(f'http://localhost:8000/get_advertisement/{id}').json()
    SUBJECT = "Cloud Computing HW1"

    if result:
        TEXT = f"""
        <h1>Your ad has been accepted! </h1>
        <h2> category: vehichel </h2>
        <a href="{get_url(response['address'])}">image url: {get_url(response['address'])}</a>
        """
    else:
        TEXT = "<h1>Your ad has been denied:( </h1>"
    send_simple_message(response["email"], SUBJECT, TEXT)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
