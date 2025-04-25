import pika
import json
from app.database import SessionLocal
from app.models import ProductReturn
from datetime import datetime

def callback(ch, method, properties, body):
    try:
        data = json.loads(body.decode("utf-8"))
        print("[InventoryService] Evento ShipmentReturned recibido:", data)

        db = SessionLocal()

        new_return = ProductReturn(
            product_id=data["product_id"],
            quantity=data["quantity"],
            reason="unknown",
            timestamp=datetime.utcnow()
        )

        db.add(new_return)
        db.commit()
        db.close()

    except Exception as e:
        print(f"Error al procesar devolución: {e}")


def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="ordico_exchange", exchange_type="topic")
    channel.queue_declare(queue="inventory_return_queue")
    channel.queue_bind(exchange="ordico_exchange", queue="inventory_return_queue", routing_key="event.ShipmentReturned")

    print("Esperando eventos 'ShipmentReturned' en InventoryService...")
    channel.basic_consume(queue="inventory_return_queue", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == "__main__":
    start_consumer()
