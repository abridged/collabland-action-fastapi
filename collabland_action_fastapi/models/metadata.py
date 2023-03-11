from typing import List, Optional
from pydantic import BaseModel


# The mini-app version model
class Version(BaseModel):
    name: str


# The mini-app supported interactions model
class SupportedInteractions(BaseModel):
    type: int
    names: Optional[List[str]]
    ids: Optional[List[str]]


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
