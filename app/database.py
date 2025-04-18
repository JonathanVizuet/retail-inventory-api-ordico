from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase

DATABASE_URL = "mssql+pyodbc://sa:Ordico2024!@localhost:1433/OrdicoRetailInventory?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db() -> Session:
    db =  SessionLocal()
    try:
        yield db
    finally:
        db.close()