from sqlalchemy import create_engine, Engine, event
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from database import DB_NAME

engine = create_engine(f'sqlite:///{DB_NAME}')
Session = sessionmaker(bind=engine)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class Base(DeclarativeBase):
    pass


def create_tables():
    Base.metadata.create_all(engine)
