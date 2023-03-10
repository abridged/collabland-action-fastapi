from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from discord.enums import InteractionType

hello_action_router = APIRouter(
    prefix="/hello-action",
    tags=["hello-action"],
)


# The mini-app version model
class Version(BaseModel):
    name: str


# The mini-app supported interactions model
class SupportedInteractions(BaseModel):
    type: int
    names: List[str]


class Manifest(BaseModel):
    appId: str
    developer: str
    name: str
    platforms: List[str]
    shortName: str
    version: Version
    website: str
    description: str


class Metadata(BaseModel):
    manifest: Manifest
    supportedInteractions: List[SupportedInteractions]


@hello_action_router.get("/metadata")
async def get_hello_action_metadata() -> Metadata:
    return {
        "manifest": {
            "appId": "hello-action",
            "developer": "collab.land",
            "name": "HelloAction",
            "platforms": ["discord"],
            "shortName": "hello-action",
            "version": {"name": "0.0.1"},
            "website": "https://collab.land",
            "description": "An example Collab.Land action",
        },
        "supportedInteractions": [
            {
                "type": InteractionType.application_command.value,
                "names": ["hello-action"],
            }
        ],
    }
