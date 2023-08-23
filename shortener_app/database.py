# shortener_app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

engine = create_engine( # Entrypoint to the database
    get_settings().db_url, connect_args={"check_same_thread": False}
) # check_same_thread allows more than one connection at a time

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
) # Create a database session class

Base = declarative_base()
# Returns a class that connects the database engine to the SQLAlchemy
# functionality of the models
# Base will be the class that the database models inherit from