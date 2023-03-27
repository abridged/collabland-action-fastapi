#!/usr/bin/env python
from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import time
from datetime import datetime
from .hello_action.main import hello_action_router
from .button_action.main import button_action_router
from .popup_action.main import popup_action_router
from dotenv import load_dotenv
from os import getenv
from .utils.signature import SignatureVerifier

load_dotenv()
startTime = time.time()

tags_metadata = [
    {"name": "root", "description": "Healthcheck API Route"},
    {
        "name": "hello-action",
        "description": "API Routes dealing with the **/hello-action** slash command.",
    },
    {
        "name": "button-action",
        "description": "API Routes dealing with the **/button-action** slash command.",
    },
    {
        "name": "popup-action",
        "description": "API Routes dealing with the **/popup-action** slash command.",
    },
]
app = FastAPI(
    title="Collab.Land Action Python Template",
    description="An example of how to write APIs utilizing Collab.Land Actions in Python",
    version="0.1.0",
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log(req: Request, call_next):
    if req.url.path.endswith("/interactions") and req.method == "POST":
        SignatureVerifier()
    res = await call_next(req)
    return res


@app.get("/", tags=["root"])
async def root():
    return {
        "success": True,
        "uptime": time.time() - startTime,
        "timestamp": datetime.now().isoformat(),
    }


app.include_router(
    hello_action_router, dependencies=[Depends(SignatureVerifier.verify_signature)]
)
app.include_router(
    button_action_router, dependencies=[Depends(SignatureVerifier.verify_signature)]
)
app.include_router(
    popup_action_router, dependencies=[Depends(SignatureVerifier.verify_signature)]
)


def start():
    uvicorn.run(
        "collabland_action_fastapi.main:app",
        host="0.0.0.0",
        port=int(getenv("PORT")),
        reload=False if getenv("SERVER_ENV") == "production" else True,
    )
