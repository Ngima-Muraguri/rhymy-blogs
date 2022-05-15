import os

BASE_DIR = os.path.abspath(__name__)

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + 