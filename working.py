from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
  return {"Data": "Hello World"}

@app.get("/about")
def about():
  return {"Data": "About"}
