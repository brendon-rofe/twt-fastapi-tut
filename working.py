from fastapi import FastAPI
from inventory_data import inventory

app = FastAPI()

@app.get("/")
def home():
  return {"Data": "Hello World"}

@app.get("/item/{item_id}")
def get_item(item_id: int):
  return inventory[item_id]

@app.get("/get-by-name")
def get_by_name(name: str = None):
  for item_id in inventory:
    if inventory[item_id]["name"] == name:
      return inventory[item_id]
  return {"Data": "Not found"}

@app.post("/create-item")
def create_item():
  return
