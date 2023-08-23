# shortener_app/main.py

from fastapi import FastAPI

app = FastAPI()

# To run 
# uvicorn shortener_app.main:app --reload

@app.get("/") # path operation decorator
def read_root():
    return "Welcome to the Short URL API :)"