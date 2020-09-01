from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declaritive import declaritive_base

db = create_engine("postgres://dec@localhost/url_test")

Session = sessionmaker(db)

Base = declaritive_base()
