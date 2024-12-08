from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessrionmaker


DATABASE_URL = "postgresql://username:password@localhost:5432/taskdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessrionmaker(autocommit=False, autoFlush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    