from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
host=os.environ["host"] 
database=os.environ["database"]
user=os.environ["user"],
password=os.environ["password"]
  
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/baseprojetopessoal')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Pessoas(Base):
    __tablename__ = "pessoas"

    name: Column(String, nullable=False)
    age: Column(Integer, nullable=False)

    def __repr__(self):
        return f"Pessoa (Nome:{self.name}, Idade:{self.age})"
    
#Select
data = session.query(Pessoas).all()
print(data)