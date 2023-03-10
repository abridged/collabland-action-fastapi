#!/usr/bin/env python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import time
from datetime import datetime
from .hello_action.main import hello_action_router

startTime = time.time()
tags_metadata = [
    {"name": "root", "description": "Healthcheck API Route"},
    {
        "name": "hello-action",
        "description": "API Routes dealing with the **/hello-action** slash command.",
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


@app.get("/", tags=["root"])
async def root():
    return {
        "success": True,
        "uptime": time.time() - startTime,
        "timestamp": datetime.now().isoformat(),
    }


app.include_router(hello_action_router)


def start():
    uvicorn.run(
        "collabland_action_fastapi.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
