from typing import Any, Dict
from fastapi import APIRouter
from discord.enums import (
    InteractionType,
    AppCommandType,
    ButtonStyle,
    InteractionResponseType,
    ComponentType,
)
from ..models.metadata import Metadata
from discord.ui import Button, View

button_action_router = APIRouter(
    prefix="/button-action",
    tags=["button-action"],
)


@button_action_router.get("/metadata")
async def get_button_action_metadata() -> Metadata:
    return {
        "manifest": {
            "appId": "button-action",
            "developer": "collab.land",
            "name": "ButtonAction",
            "platforms": ["discord"],
            "shortName": "button-action",
            "version": {"name": "0.0.1"},
            "website": "https://collab.land",
            "description": "An example Collab.Land action",
        },
        "supportedInteractions": [
            {
                "type": InteractionType.application_command.value,
                "names": ["button-action"],
            },
            {"type": InteractionType.component.value, "ids": ["test-button"]},
        ],
        "applicationCommands": [
            {
                "metadata": {"name": "ButtonAction", "shortName": "button-action"},
                "name": "button-action",
                "type": AppCommandType.chat_input.value,
                "description": "/button-action",
                "options": [],
            }
        ],
    }


@button_action_router.post("/interactions")
async def post_button_action_interaction(req: Dict[str, Any]):
    parsed_req = dict(req)
    interaction_type = int(parsed_req.get("type"))
    if interaction_type == InteractionType.application_command.value:
        button = Button(
            style=ButtonStyle.green,
            label="Click Me!",
            custom_id="test-button",
            disabled=False,
            row=1,
        )
        view = View()
        view.add_item(button)
        components = view.to_components()
        return {
            "type": InteractionResponseType.channel_message.value,
            "data": {
                "flags": 1 << 6,
                "content": "Click the button below, to test the interaction!",
                "components": components,
            },
        }
    elif interaction_type == InteractionType.component.value:
        return {
            "type": InteractionResponseType.channel_message.value,
            "data": {
                "flags": 1 << 6,
                "content": "Button was clicked!",
            },
        }
