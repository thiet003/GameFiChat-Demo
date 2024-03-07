from fastapi import FastAPI, Request, HTTPException, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from os import urandom
from time import time
import uvicorn
import json
from requests import get
from requests import post 
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from json import dumps
from time import time
from flask import request
from hashlib import sha256
from datetime import datetime
from json     import loads
import os
from config import special_instructions
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from RAG.query import process

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả các origin, điều chỉnh cho phù hợp với nhu cầu của bạn
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả các method, bao gồm cả OPTIONS
    allow_headers=["*"],
)

class Part(BaseModel):
    content: str
    role: str

class MetaContent(BaseModel):
    conversation: List[Dict[str, Any]] = []
    internet_access: bool = Field(default=False)
    content_type: str = Field(default="text")
    parts: List[Part]
class Meta(BaseModel):
    id: int
    content: MetaContent
class ConversationRequest(BaseModel):
    conversation_id: str
    action: str
    model: str
    jailbreak: str
    meta: Meta

def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

config = load_config()
site_config = config['site_config']

# Bien moi truong
openai_key = config['openai_key']
openai_api_base = config['openai_api_base']


def call_openai_streaming(
    client, gpt_model_name, messages, temperature, response_format, final_response
):
    openai_stream = client.chat.completions.create(
        model=gpt_model_name,
        messages=messages,
        stream=True,
        temperature=temperature,
        response_format=response_format,
    )
    for chunk in openai_stream:
        if chunk.choices[0].delta.content is not None:
            final_response += chunk.choices[0].delta.content
            yield chunk.choices[0].delta.content


def qa_conversation(request_data: ConversationRequest):
    jailbreak = request_data.jailbreak
    internet_access = request_data.meta.content.internet_access
    _conversation = request_data.meta.content.conversation
    prompt = request_data.meta.content.parts[0]
    system_prompt = """
        You are a helpful, friendly and informative assistant. 
        If the user say as hi, hello, alo,..., you can say hi back and introduce yourself as 'GameFi Assistant'.
        If a user comments or thanks for the reply, respond openly and friendly.
        If the context is not empty, then the context is the information you have about the user's question. 
        Use that information and the topic of the question to generate an informative response.
        If user ask a question and the contex is empty, reply 'Sorry I don't know'
        When answering, don't say 'Based on the context I was given'. 
        !!! Do not say that you answer the question with the context, just answer the question.
    """
    res = process(prompt.content, _conversation) 
    print(res)
    prompt = f"Please answer this question: {prompt.content}\n\nhere's the context you should use:\n\n{res}"
    messages = [{"role": "system", "content": system_prompt}] + _conversation + [{"role": "user", "content": prompt}]
    def llm_call(messages): 
        final_response = ""
        client = OpenAI(api_key=openai_key)
        yield from call_openai_streaming(
            client, request_data.model,
            messages, 0.0, None, final_response
        )
    return llm_call(messages)

@app.post("/backend/v2/request")
async def conversation(request: Request):
    request_data = await request.json()
    request_obj = ConversationRequest(**request_data)
    headers = {
        "Content-Type": "text/plain",
        "Transfer-Encoding": "chunked",
        "Connection": "Transfer-Encoding",
    }
    generator = qa_conversation(request_obj)
    return StreamingResponse(generator, media_type="text/plain", headers=headers)


if __name__ == "__main__":
    uvicorn.run("run:app", host=site_config.get('host', '127.0.0.1'), port=site_config.get('port', 8000), reload=site_config.get('debug', False))