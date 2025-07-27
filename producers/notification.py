from connection import RabbitMQConnection
from config import Config
from producers.base import RabbitMQProducer

def send_notification():
    user_notifications={

        "user1": {
            "notifications":{"email": True, "sms": False},
            "email":"user1@example.com",
            "phone":"123456789",
                        
        },
         "user2": {
            "notifications":{"email": True, "sms": True},
            "email":"user2@example.com",
            "phone":"987654321",
                        
        },
          "user3": {
            "notifications":{"email": False, "sms": True},
            "email":"user3@example.com",
            "phone":"10101010101010101",
                        
        },

    }


    config=Config(override=True)

    with RabbitMQConnection(host=config.RABBITMQ_HOST, port=config.RABBITMQ_PORT, username=config.RABBITMQ_USER,
        password=config.RABBITMQ_PASSWORD) as connection:

        producer=RabbitMQProducer(connection)
        for user_id, user_data in user_notifications.items():
            notification=user_data["notifications"]
            email=user_data["email"]
            phone=user_data["phone"]

            for notificatoin_type, enables in notification.items():
                if enables:
                    routing_key=f"notif.{notificatoin_type}"


                    data={
                    "user_id":user_id,
                    "type":notificatoin_type,
                    "email":email,
                    "phone":phone,


                    }


                    producer.publish_message(exchange=config.EXCHANGE_NAME, routing_key=routing_key, data=data)
                    print(f"Notification sent to user {user_id} via {notificatoin_type}")





    




