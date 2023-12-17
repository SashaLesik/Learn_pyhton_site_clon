import os
from dotenv import load_dotenv

load_dotenv()
try:
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'default_password')
except KeyError:
    print('не найдена переменная')
    raise
