import pika
import json

def publish_event(event_name: str, payload: dict):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.exchange_declare(exchange="ordico_exchange", exchange_type="topic")

    message = json.dumps(payload)
    routing_key = f"event.{event_name}"
    channel.basic_publish(exchange="ordico_exchange", routing_key=routing_key, body=message)

    print(f"Evento enviado: {event_name} -> {message}")
    connection.close()