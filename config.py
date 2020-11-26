import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

base_dir = os.path.abspath(os.path.dirname(__file__))

db = os.environ["DATABASE_NAME"]
user = os.environ["DATABASE_USER"]
password = os.environ["DATABASE_PASS"]
host = os.environ["DATABASE_HOST"]
port = os.environ["DATABASE_PORT"]


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'pachaqtec'
    SQLALCHEMY_DATABASE_URI = f'postgres://{user}:{password}@{host}:{port}/{db}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
