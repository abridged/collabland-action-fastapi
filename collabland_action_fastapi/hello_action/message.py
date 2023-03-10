from asyncio import sleep
import requests
from discord.enums import InteractionResponseType


async def handle_message(callback_url: str, message: str):
    follow = Followup(callback_url, message)
    await follow.followup()
    await follow.edit()
    await follow.delete()


class Followup:
    def __init__(self, callback_url: str, message: str) -> None:
        self.callback_url = str(callback_url)
        self.msg_id = ""
        self.message = str(message)

    async def followup(self):
        await sleep(1)
        payload = {
            "content": f"**Following up :eyes:? ::** {self.message}",
            "flags": 1 << 6,
            "type": InteractionResponseType.channel_message.value,
        }
        response = requests.post(self.callback_url, json=payload)
        response_json = response.json()
        self.msg_id = response_json.get("id")

    async def edit(self):
        for x in ["five", "four", "three", "two", "one"]:
            payload = {
                "type": InteractionResponseType.channel_message.value,
                "flags": 1 << 6,
                "content": f"**Deleting the message in :{x}: ::** {self.message}",
            }
            requests.patch(f"{self.callback_url}/messages/{self.msg_id}", json=payload)
            await sleep(1)

    async def delete(self):
        requests.delete(f"{self.callback_url}/messages/{self.msg_id}")
