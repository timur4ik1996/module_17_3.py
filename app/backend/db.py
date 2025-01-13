# Задача "Модели SQLAlchemy":
# База данных и движок:


from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import Column,Integer,String


engine=create_engine("sqlite:///taskmanager.db",echo=True)

SessionLocal=sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    age=Column(Integer)
