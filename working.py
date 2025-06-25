from fastapi import FastAPI
from inventory_data import inventory

app = FastAPI()

@app.get("/")
def home():
  return {"Data": "Hello World"}


