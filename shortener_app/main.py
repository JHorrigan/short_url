# shortener_app/main.py

import secrets

import validators
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

app = FastAPI()
# Bind your database engine, will create if doesnt exist
# with all modelled tables
models.Base.metadata.create_all(bind=engine)

def get_db(): # Create & yield a new db session with each request
    db = SessionLocal()
    try:
        yield db
    finally: # Close the connection whether an error occurs or not
        db.close()

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

@app.get("/") # path operation decorator
def read_root():
    return "Welcome to the Short URL API :)"

@app.post("/url", response_model=schemas.URLInfo) # Post a valid target url
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    # By passing get_db to Depends, this request will use and close a db session
    # pydantic checks if URL is a string, but not if it is a valid url
    # So here we use validators
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")

    # Provide random strings for key & secret_key
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))

    # Create a database entry for the target url
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    # Add key and secret key to match required URLInfo schema for response
    db_url.url = key
    db_url.admin_url = secret_key

    return db_url