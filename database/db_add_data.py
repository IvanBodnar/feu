from database.db_main import engine, Hechos
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


