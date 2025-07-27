import os
from dotenv import load_dotenv




class Config:
    _instance=None

    def __new__(cls,*args,**kwargs):

        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.__initialized=False

        return cls._instance

    def __init__(self, load_from_file=True, override=False):
        if self.__initialized and not override:
            return

        self.RUN_MODE=os.environ.get('RUN_MODE','debug')

        

        if load_from_file:
            env_file_path=self.RUN_MODE + '.env'
            load_dotenv(env_file_path)




        self.RABBITMQ_HOST=os.environ.get('RABBITMQ_HOST','localhost')
        self.RABBITMQ_PORT=os.environ.get('RABBITMQ_PORT',5672)
        self.RABBITMQ_USER=os.environ.get('RABBITMQ_USER','admin')
        self.RABBITMQ_PASSWORD=os.environ.get('RABBITMQ_PASSWORD','admin')
        self.RABBITMQ_VHOST=os.environ.get('RABBITMQ_VHOST','localhost')
        self.EXCHANGE_NAME=os.environ.get('EXCHANGE_NAME','notification_exchange')



        self.__initialized=True



        
    def is_test_mode(self):
        return self.RUN_MODE=='test'


    def is_debug_mode(self):
        return self.RUN_MODE=='debug'


    def waiting_factor(self):

        if self.is_test_mode():
            return 0

        return 2

        
