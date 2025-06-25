from fastapi import FastAPI
from inventory_data import inventory

app = FastAPI()

@app.get("/")
def home():
  return {"Data": "Hello World"}

@app.get("/item/{item_id}")
def get_item(item_id: int):
  return inventory[item_id]
