import hashlib
import time

from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, String
from constants import token

from .base import Base


class Token(Base):
    __tablename__ = 'token'

    user_id = Column(String(36), ForeignKey("user.id"), nullable=False)
    content = Column(String(64), nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    deleted_at = Column(DateTime)

    def __init__(self, user_id:str):
        self.user_id = user_id

        current_time = time.time()

        hash = hashlib.md5()
        hashlib.update(bytes(token.SALT + current_time))

        self.content = hash.hexdigest()
        
        self.expiration_date = datetime.fromtimestamp(current_time + token.TTL)
