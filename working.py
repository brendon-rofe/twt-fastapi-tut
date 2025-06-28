from fastapi import FastAPI
from inventory_data import inventory
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  type: Optional[str] = None

class UpdateItem(BaseModel):
  name: Optional[str] = None
  price: Optional[float] = None
  type: Optional[str] = None

@app.get("/")
def home():
  return {"Data": "Hello World"}

@app.get("/item/{item_id}")
def get_item(item_id: int):
  return inventory[item_id]

@app.get("/items")
def get_all_items():
  return inventory

@app.get("/get-by-name")
def get_by_name(name: str = None):
  for item_id in inventory:
    if inventory[item_id]["name"] == name:
      return inventory[item_id]
  return {"Data": "Not found"}

@app.post("/create-item")
def create_item(item: Item):
  new_id = len(inventory) + 1;
  inventory[new_id] = {
    "name": item.name,
    "price": item.price,
    "type": item.price
  }
  with open("inventory_data.py", "w") as f:
    f.write(f"inventory = {inventory}")

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
  if item_id not in inventory:
    return { "Error": "Item ID does not exist" }
  else:
    inventory[item_id].update(item)
    
    with open("inventory_data.py", "w") as f:
      f.write(f"inventory = {inventory}")

@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
  if item_id in inventory:
    del inventory[item_id]
    with open("inventory_data.py", "w") as f:
      f.write(f"inventory = {inventory}")
  else:
    return { "Error": "Item ID does not exist" }
