import os
from dotenv import load_dotenv
load_dotenv()

class BaseConfig():
   API_PREFIX = '/api'
   TESTING = False
   DEBUG = False
#    DB_HOST=os.getenv('DB_HOST')
#    DB_USERNAME=os.getenv('DB_USERNAME')
#    DB_PASSWORD=os.getenv('DB_PASSWORD')
#    DATABASE_NAME=os.getenv('DATABASE_NAME')

class DevConfig(BaseConfig):
   FLASK_ENV = 'development'
   DEBUG = True

class ProductionConfig(BaseConfig):
   FLASK_ENV = 'production'

class TestConfig(BaseConfig):
   FLASK_ENV = 'development'
   TESTING = True
   DEBUG = True
