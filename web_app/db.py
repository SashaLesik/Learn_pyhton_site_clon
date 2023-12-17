from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker



DATABASE = 'postgres'
HOST = 'localhost'
PORT = '5432'

connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(connection_string)
db_session = scoped_session(sessionmaker(bind=engine))

Base = sqlalchemy.orm.declarative_base()
Base.query = db_session.query_property()
