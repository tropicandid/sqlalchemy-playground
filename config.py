import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.environ.get('FLASK_KEY')
    SQLALCHEMY_ECHO=True
    ALEMBIC_CONTEXT = {"render_as_batch":True} # If you are not using sqlite, you dont' need this