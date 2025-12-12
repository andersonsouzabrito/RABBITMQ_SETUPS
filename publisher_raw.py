import pika

conn_param = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=pika.PlainCredentials(
        username='guest',
        password='guest'
    )
)

channel = pika.BlockingConnection(conn_param).channel()

channel.basic_publish(
    exchange="data_exchange",
    routing_key="",
    body="mandandoDenovo",
    properties=pika.BasicProperties(
        delivery_mode=2
    )
)