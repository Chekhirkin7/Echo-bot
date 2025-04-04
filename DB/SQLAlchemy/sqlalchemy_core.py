from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData, DateTime, func, BigInteger
import os
from dotenv import load_dotenv

metadata = MetaData()

load_dotenv()

PG_HOST = os.getenv("PG_HOST")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_PORT = os.getenv("PG_PORT")
PG_USER = os.getenv("PG_USER")
PG_DB = os.getenv("PG_ALCH_DB")

engine = create_engine(f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}")


users = Table('users', metadata,
			  Column('id', BigInteger, primary_key=True),
			  Column('username', String(34)),
			  Column('email', String(50)),
			  Column('phone', String(20)),
			  Column('created_at', DateTime, server_default=func.now()),
)


messages = Table('messages', metadata,
			  Column('id', Integer, primary_key=True, autoincrement=True),
			  Column('user_id', BigInteger, ForeignKey('users.id')),
			  Column('message_text', String),
			  Column('created_at', DateTime, server_default=func.now()),
)

metadata.drop_all(engine)
metadata.create_all(engine)
