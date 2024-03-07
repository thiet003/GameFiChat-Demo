from fastapi import FastAPI, Request, HTTPException, Depends, Form, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from os import urandom
from time import time
import uvicorn
import json
from json import loads
from requests import get
from requests import post 
import httpx


app = FastAPI()

def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

config = load_config()
site_config = config['site_config']

# Xử lí các assets
templates = Jinja2Templates(directory = "client/html")
app.mount("/assets", StaticFiles(directory="client"), name="assets")

# Hàm render trang chat với chat_id
@app.get("/chat/{conversation_id}", response_class=HTMLResponse)
async def chat(request: Request, conversation_id: str):
    if '-' not in conversation_id:
        return RedirectResponse(url="/chat")
    return templates.TemplateResponse("index.html", {"request": request, "chat_id": conversation_id})

# Hàm render trang index với chat_id mới
@app.get('/chat/')
async def index(request: Request):
    chat_id = f'{urandom(4).hex()}-{urandom(2).hex()}-{urandom(2).hex()}-{urandom(2).hex()}-{hex(int(time() * 1000))[2:]}'
    return templates.TemplateResponse("index.html", {"request": request})

# Redirect từ root đến /chat/
@app.get("/", response_class=HTMLResponse)
async def root():
    return RedirectResponse(url="/chat/")

async def stream_response(request_data):
    url = 'http://127.0.0.1:2003/backend/v2/request'
    timeout = 20.0
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("POST", url, json=request_data) as response:
            async for chunk in response.aiter_bytes():
                print(chunk)
                yield chunk
@app.post("/backend-api/v2/conversation")
async def conversation(request: Request):
    request_data = await request.json()
    return StreamingResponse(stream_response(request_data), media_type='text/event-stream')

if __name__ == "__main__":
    uvicorn.run("app:app", host=site_config.get('host', '127.0.0.1'), port=site_config.get('port', 8000), reload=site_config.get('debug', False))