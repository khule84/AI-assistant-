from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r") as file:
        return file.read()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Market Insights API Running"}

