import hashlib

from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column("id", String(36), primary_key=True)
    name = Column(String(128), nullable=False)
    email = Column(String(64), nullable=False)
    login = Column(String(32), nullable=False)
    password = Column(String(64), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    deleted_at = Column(DateTime)

    children = relationship("Token")

    def __init__(self, name:str, email:str, login:str, password:str):
        self.name = name
        self.email = email
        self.login = login

        hash = hashlib.md5()
        hashlib.update(bytes(password))

        self.password = hash.hexdigest()
