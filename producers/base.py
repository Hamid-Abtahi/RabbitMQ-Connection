import json
from pika import BasicProperties, exceptions as pika_exceptions

from connection import RabbitMQConnection




class RabbitMQProducer:

    def __init__(self,connection):

        self.connection=connection
        self.channel=None



    def publish_message(self, exchange, routing_key, data):
        if self.channel is None:
            self.channel=self.connection.get_channel()

        if self.channel is not None:
            try:
                self.channel.exchange_declare(exchange=exchange, exchange_type="topic")
                message=json.dumps(data)
                properties=BasicProperties(content_type="application/json", delivery_mode=2)
                self.channel.basic_publish(
                    exchange=exchange,
                    routing_key=routing_key,
                    body=message,
                    properties=properties,
                )
                print(f"Message sent to exchange: {exchange} with routing_key {routing_key}")
            except pika_exceptions.ConnectionClosedByBroker:
                print("Connection closed by broker. Failed to publish the message")
        else:
            print("Failed to obtain a channel for publishing the message")