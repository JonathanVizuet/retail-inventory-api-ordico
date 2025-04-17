from app.database import engine

try:
    with engine.connect() as connection:
        print("Conexión exitosa a SQL Server")
except Exception as e:
    print("Error de conexión:", e)
