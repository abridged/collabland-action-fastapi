from typing import Any, Dict
from fastapi import APIRouter
from discord.enums import (
    InteractionType,
    AppCommandType,
    ButtonStyle,
    InteractionResponseType,
    ComponentType,
    TextStyle,
)
from discord.ui import Modal, TextInput
from ..models.metadata import Metadata

popup_action_router = APIRouter(
    prefix="/popup-action",
    tags=["popup-action"],
)


@popup_action_router.get("/metadata")
async def get_popup_action_metadata() -> Metadata:
    return {
        "manifest": {
            "appId": "popup-action",
            "developer": "collab.land",
            "name": "PopUpAction",
            "platforms": ["discord"],
            "shortName": "popup-action",
            "version": {"name": "0.0.1"},
            "website": "https://collab.land",
            "description": "An example Collab.Land action",
        },
        "supportedInteractions": [
            {
                "type": InteractionType.application_command.value,
                "names": ["popup-action"],
            },
            {"type": InteractionType.modal_submit.value, "ids": ["submit"]},
        ],
        "applicationCommands": [
            {
                "metadata": {"name": "PopUpAction", "shortName": "popup-action"},
                "name": "popup-action",
                "type": AppCommandType.chat_input.value,
                "description": "/popup-action",
                "options": [],
            }
        ],
    }


@popup_action_router.post("/interactions")
async def post_popup_action_interaction(req: Dict[str, Any]):
    parsed_req = dict(req)
    interaction_type = int(parsed_req.get("type"))
    if interaction_type == InteractionType.application_command.value:
        modal = Modal(custom_id="submit", title="Submit to Collab.Land Action!")
        name = TextInput(
            custom_id="your-name",
            label="Enter your name:",
            placeholder="John Doe",
            max_length=100,
            style=TextStyle.short,
            required=True,
        )
        modal.add_item(name)
        return {"type": InteractionResponseType.modal.value, "data": modal.to_dict()}
    elif interaction_type == InteractionType.modal_submit.value:
        components = parsed_req.get("data").get("components")
        name = components[0].get("components")[0].get("value")
        return {
            "type": InteractionResponseType.channel_message.value,
            "data": {
                "flags": 1 << 6,
                "content": f"Your name `{name}` was submitted!",
            },
        }
