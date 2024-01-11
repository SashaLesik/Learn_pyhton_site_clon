
import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

load_dotenv()
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.getenv('DB_PASSWORD', 'default_password')
DB_NAME = os.getenv('DB_NAME', 'postgres')
HOST = os.getenv('HOST', 'default_host')
PORT = os.getenv('PORT', 'default_port')

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{HOST}:{PORT}/{DB_NAME}')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


