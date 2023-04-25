from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
import os

load_dotenv()
host=os.environ["host"] 
database=os.environ["database"]
user=os.environ["user"],
password=os.environ["password"]
  
engine = create_engine(f'postgresql+psycopg2://postgres:postgres@{host}/{database}',isolation_level="SERIALIZABLE",)
print(engine)