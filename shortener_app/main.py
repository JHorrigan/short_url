# shortener_app/main.py

import validators
from fastapi import FastAPI, HTTPException

from . import schemas

app = FastAPI()

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

@app.get("/") # path operation decorator
def read_root():
    return "Welcome to the Short URL API :)"

@app.post("/url") # Post a valid target url
def create_url(url: schemas.URLBase):
    # pydantic checks if URL is a string, but not if it is a valid url
    # So here we use validators
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")
    return f"TODO: Create database entry for: {url.target_url}"