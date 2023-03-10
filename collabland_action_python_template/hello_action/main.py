from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from discord.enums import InteractionType, AppCommandType, AppCommandOptionType

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


# The mini-app application command metadata model
class ApplicationCommandMetadata(BaseModel):
    name: str
    shortName: str


# The mini-app application command option data model
class OptionsData(BaseModel):
    name: str
    description: str
    type: int
    required: bool


# The mini-app application commands model
class ApplicationCommands(BaseModel):
    metadata: ApplicationCommandMetadata
    name: str
    type: int
    description: str
    options: List[OptionsData]


# The mini-app manifest model
class Manifest(BaseModel):
    appId: str
    developer: str
    name: str
    platforms: List[str]
    shortName: str
    version: Version
    website: str
    description: str


# The mini-app metadata model
class Metadata(BaseModel):
    manifest: Manifest
    supportedInteractions: List[SupportedInteractions]
    applicationCommands: List[ApplicationCommands]


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
        "applicationCommands": [
            {
                "metadata": {"name": "HelloAction", "shortName": "hello-action"},
                "name": "hello-action",
                "type": AppCommandType.chat_input.value,
                "description": "/hello-action",
                "options": [
                    {
                        "name": "your-name",
                        "description": "Name of the person we're greeting",
                        "type": AppCommandOptionType.string.value,
                        "required": True,
                    }
                ],
            }
        ],
    }
