from sqlalchemy import Column, Integer, String
from db import Base,engine


class User(Base):
    __tablename__="usersss"
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True)
    hash_password = Column(String)


Base.metadata.create_all(bind=engine)
