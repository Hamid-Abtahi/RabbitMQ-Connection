import pytest
from unittest.mock import patch, MagicMock
from pika import BlockingConnection, exceptions
from connection import RabbitMQConnection
from config import Config as AppConfig



@pytest.fixture
def config():
    return AppConfig()


@pytest.fixture
def rabbitmq_connection(config):
    return RabbitMQConnection(
        host=config.RABBITMQ_HOST,
        port=config.RABBITMQ_PORT,
        username=config.RABBITMQ_USER,
        password=config.RABBITMQ_PASSWORD,
    )


def test_singleton_instance():

    connection1=RabbitMQConnection()
    connection2=RabbitMQConnection()
    assert connection1 is connection2



def test_connect_successful(rabbitmq_connection):
    
    with patch.object(BlockingConnection, "__init__", return_value=None), patch.object(BlockingConnection,
     "is_open", return_value=True):

        rabbitmq_connection.connect()
        assert rabbitmq_connection.connection is not None
        assert rabbitmq_connection.connection.is_open 
    



def test_connect_failed(rabbitmq_connection):
    
    with patch.object(BlockingConnection, "__init__", side_effect=exceptions.AMQPConnectionError("Connection failed")):

        rabbitmq_connection.connect()
        assert rabbitmq_connection.connection is None





def test_is_connected(rabbitmq_connection):
    
    with patch.object(BlockingConnection, "__init__", return_value=None), patch.object(BlockingConnection,
     "is_open", return_value=True):

        rabbitmq_connection.connect()
        assert rabbitmq_connection.is_connected()
    

def test_is_not_connected(rabbitmq_connection):
    
        assert not rabbitmq_connection.is_connected()
    



def test_close(rabbitmq_connection):
    connection_mock=MagicMock(BlockingConnection)
    rabbitmq_connection.connection=connection_mock

    rabbitmq_connection.close()
    connection_mock.close.assert_called_once()



def test_get_channel_not_connected(rabbitmq_connection):
    assert rabbitmq_connection.get_channel() is None


def test_get_channel_connected(rabbitmq_connection):
    connection_mock=MagicMock(BlockingConnection)
    rabbitmq_connection.connection=connection_mock

    channel_mock=MagicMock()
    connection_mock.channel.return_value=channel_mock

    assert channel_mock is rabbitmq_connection.get_channel()
    