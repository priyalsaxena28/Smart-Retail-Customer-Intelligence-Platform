from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.product import router as product_router
from app.sentiment import router as sentiment_router
from app.face import router as face_router
from app.chatbot import router as chatbot_router

app = FastAPI(title="Smart Retail Customer Intelligence Platform")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(product_router)
app.include_router(sentiment_router)
app.include_router(face_router)
app.include_router(chatbot_router)


from fastapi.responses import HTMLResponse

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )