import time
from pika import PlainCredentials, ConnectionParameters, BlockingConnection, exceptions
import config


class RabbitMQConnection:
    _instance=None
    def __new__(cls,host="localhost",port=5672, username="admin", password="admin"):

        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.__initialized=False

        return cls._instance


    def __init__(self, host="localhost",port=5672, username="admin", password="admin"):

        self.host="localhost"
        self.port=5672
        self.username="admin"
        self.password="admin"
        self.connection=None


    def __enter__(self):

        self.connect()
        return self

    def __exit__(self,exc_type, exc_value, traceback):

        self.close()

    def connect(self):
        retries=0
        while retries<10:

            try:
                credentials=PlainCredentials(self.username, self.password)
                parameters=ConnectionParameters(host=self.host, port=self.port, credentials=credentials)
                self.connection=BlockingConnection(parameters)
                print('connected to RabbitMQ')
                return

            except exceptions.AMQPConnectionError as e:
                print("failed to connect to RabbitMQ:", e)
                retries+=1
                wait_time=config.Config().waiting_factor()**retries
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
        print("Connection retries exceeded. Stopping execution.")

    def is_connected(self):
        
        return self.connection is not None and self.connection.is_open


    def close(self):
        
        if self.is_connected():
            self.connection.close()
            self.connection=None
            print('Closed RabbitMQ connection')



    def get_channel(self):
        
        if self.is_connected():
            return self.connection.channel()

        return None

