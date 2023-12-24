
import os
from dotenv import load_dotenv

load_dotenv()
try:
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'default_password')
except KeyError:
    print('не найдена переменная')
    raise

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'postgres'
HOST = 'localhost'
PORT = '5433'

SQLALCHEMY_DATABASE_URI = f"postgresql:/// {os.path.join(basedir, '..', 'postgres.db')}"

