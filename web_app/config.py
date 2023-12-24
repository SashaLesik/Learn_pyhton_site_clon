
import os
from dotenv import load_dotenv

load_dotenv()
try:
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'default_password')
except KeyError:
    print('не найдена переменная')
    raise

DATABASE = 'postgres'
HOST = 'localhost'
PORT = '5432'

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{HOST}:{PORT}/{DATABASE}'

