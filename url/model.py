from sqlalchemy import Column, String
from database.setup import Base


class Alias(Base):
    __tablename__ = 'aliases'

    slug = Column(String, primary_key=True)
    url = Column(String)
