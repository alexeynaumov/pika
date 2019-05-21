import pika
import time


def process_function(data):
  print("Received :\n{}".format(data))

  time.sleep(5)
  print(" Data processed")
  return;


url = "amqp://aytzrnsk:UBRrZHaH0qwS8l7dOiE3cM1ncK8LNdzn@bulldog.rmq.cloudamqp.com/aytzrnsk"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channel
channel.queue_declare(queue='main_queue')  # declare a queue


def callback(ch, method, properties, body):
    print("channel    : {}".format(channel))
    print("method     : {}".format(method))
    print("properties : {}".format(properties))
    print("body       : {}".format(body))

    process_function(body)


# set up subscription on the queue
channel.basic_consume(
    on_message_callback=callback,
    queue='main_queue'
)

# start consuming
channel.start_consuming()
connection.close()
