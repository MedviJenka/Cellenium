import json
from dataclasses import dataclass, field
from fastapi import FastAPI, HTTPException, Response


app = FastAPI()


@dataclass
class Channel:

    id: str
    name: str
    tags: list[str] = field(default_factory=list)
    description: str = ''


channels: dict[str, Channel] = {}


with open('channels.json', encoding='utf-8') as file:
    channels_raw = json.load(file)
    for channel_raw in channels_raw:
        channel = Channel(**channel_raw)
        channels[channel.id] = channel


@app.get('/')
def get_root() -> Response:
    return Response("everything is running")


@app.get('channels/{channel_id}', response_model=Channel)
def read_item(channel_id: str) -> Channel:
    if channel_id not in channels:
        raise HTTPException(status_code=404, detail="channel not found")
    return channels[channel_id]
