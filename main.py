from fastapi import FastAPI, Body
from GetResource import get_resource

app = FastAPI()

@app.get("/")
def read():
    return {"Result": "ok"}

@app.get("/resource")
def resource():
    return get_resource()