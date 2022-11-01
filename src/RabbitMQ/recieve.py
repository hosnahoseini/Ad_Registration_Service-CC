AMQP_URL = "amqps://relnkbli:IvN1Fs_czxR2-zOw8qm3X0e8TCMjk5Jf@beaver.rmq.cloudamqp.com/relnkbli"
import imp
import pika, sys, os
from src.db.postgres import advertisements_table, database
from src.api.immega import return_category
import database

def main():
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='advertisements')

    async def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        # recive img from s3
        category = return_category()

        if (category == "car"):
            state = "confirmed"
        else:
            state = "denied"

        query = (
        advertisements_table
        .update()
        .where(id == advertisements_table.c.id)
        .values(state=state,
                category=category)

        .returning(advertisements_table.c.id)
        )
        return await database.execute(query=query)

    channel.basic_consume(queue='advertisements', on_message_callback=callback, auto_ack=True)

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