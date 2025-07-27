# RabbitMQ Connection Project

This is a simple and clean Python project designed to establish a connection with **RabbitMQ**.  
It follows **best practices** such as separation of concerns and object-oriented design patterns.

## Features

- Uses the **Singleton Pattern** for managing RabbitMQ connection.
- The **Producer** and **Consumer** are implemented as separate, independent classes.
- A dedicated class handles the **RabbitMQ configuration**.
- Each component is modular and adheres to the **SOLID principles**.
- Designed with **scalability** and **maintainability** in mind.

## Project Structure
rabbitmq_connection_project/
│
├── config/
│ └── rabbit_config.py # Configuration handler for RabbitMQ
│
├── connection/
│ └── rabbit_connection.py # Singleton-based connection class
│
├── producer/
│ └── producer.py # Separate producer class
│
├── consumer/
│ └── consumer.py # Separate consumer class
│
└── main.py # Entry point for testing or execution



## How to Use

1. Make sure RabbitMQ is up and running on your machine or network.
2. Install dependencies (if any).
3. Import the relevant classes and start producing or consuming messages.

```python
from connection.rabbit_connection import RabbitMQConnection
from producer.producer import MyProducer
from consumer.consumer import MyConsumer
