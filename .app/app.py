from config import settings
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# FastAPI
app = FastAPI(
    title=settings.name, description=settings.description, version=settings.version
)

# Jinja2Templates
templates = Jinja2Templates(directory="D:/CompSci/Projects/lostark-bot/app/templates/")

# Routes
@app.get("/")
async def root():
    return {"message": "Hello World"}
