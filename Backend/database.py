from sqlalchemy import create_engine, Column, String, Integer, delete
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
host=os.environ["host"] 
database=os.environ["database"]
user=os.environ["user"],
password=os.environ["password"]

Base = declarative_base()

class Pessoas(Base):
    __tablename__ = "pessoas"

    id = Column("id", Integer, primary_key=True, nullable=False)
    name = Column("name", String, nullable=False)
    age = Column("age", Integer, nullable=False)

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.age})"

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/baseprojetopessoal')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

#Insert na tabela Pessoas
pessoa1 = Pessoas(1, "Arthur", 21)
pessoa2 = Pessoas(2, "Carlos", 30)
session.add_all([pessoa1, pessoa2])
session.commit()

#Select todos os registros da tabela Pessoas
for row in session.query(Pessoas).all():
    print(row)

#Deletar registros