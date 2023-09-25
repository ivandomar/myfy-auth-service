from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import os

from models import Base, User, Token

db_path = "database/data"

if not os.path.exists(db_path):
   os.makedirs(db_path)

db_url = f'sqlite:///{db_path}/myfy_auth.sqlite3'

engine = create_engine(db_url, echo=True)

Session = sessionmaker(engine, expire_on_commit=False)

if not database_exists(engine.url):
    create_database(engine.url) 

    Base.metadata.create_all(engine)
