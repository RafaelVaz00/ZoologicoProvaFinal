from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:8080/zoologico"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
