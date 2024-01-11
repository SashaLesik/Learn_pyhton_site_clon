
import os
from dotenv import load_dotenv

load_dotenv()
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.getenv('DB_PASSWORD', 'default_password')
DB_NAME = os.getenv('DB_NAME', 'postgres')
HOST = os.getenv('HOST', 'default_host')
PORT = os.getenv('PORT', 'default_port')

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{HOST}:{PORT}/{DB_NAME}'



