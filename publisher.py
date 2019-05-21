import pika
import logging

logging.basicConfig()

url = "amqp://aytzrnsk:UBRrZHaH0qwS8l7dOiE3cM1ncK8LNdzn@bulldog.rmq.cloudamqp.com/aytzrnsk"
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)  # connect to CloudAMQP
channel = connection.channel()  # start a channel
channel.queue_declare(queue='main_queue')  # declare a queue

# send a message
channel.basic_publish(
    exchange='',
    routing_key='main_queue',
    body='Here goes some users data'
)

print("[x] Message sent to consumer")

connection.close()
