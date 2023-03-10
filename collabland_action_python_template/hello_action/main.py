from fastapi import APIRouter
from discord.enums import InteractionType, AppCommandType, AppCommandOptionType
from ..models.metadata import Metadata

hello_action_router = APIRouter(
    prefix="/hello-action",
    tags=["hello-action"],
)


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
