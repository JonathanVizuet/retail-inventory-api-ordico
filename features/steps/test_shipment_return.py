from behave import given, when, then
import requests
import time
import pyodbc

@given('un envío existente con estado "pending"')
def step_given_pending_shipment(context):
    context.shipment_id = 18

@when('se actualiza su estado a "return"')
def step_when_return_status(context):
    url = f"http://localhost:8001/shipments/{context.shipment_id}/status"
    response = requests.put(url, params={"new_status": "return"})
    context.response = response
    time.sleep(2)

@then('se debe recibir un evento ShipmentReturned')
def step_then_event_received(context):
    assert context.response.status_code == 200
    assert "return" in context.response.text.lower()

@then('se debe registrar una devolución en la tabla "product_returns"')
def step_then_check_db(context):
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=OrdicoRetailInventory;"
        "UID=sa;"  
        "PWD=Ordico2024!;"
        "TrustServerCertificate=yes;"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM product_returns WHERE product_id = ?", (2,))
    count = cursor.fetchone()[0]
    assert count > 0
    conn.close()
