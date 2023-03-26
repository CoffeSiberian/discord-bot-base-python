from pydantic import BaseModel

class Settings(BaseModel):
    bot_token: str
    github: str