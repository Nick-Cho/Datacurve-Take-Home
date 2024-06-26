from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_username = ""
db_password = ""
db_url = ""
db_name = ""

database_url = f'mysql+pymysql://{db_username}:{db_password}@{db_url}/{db_name}'

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()