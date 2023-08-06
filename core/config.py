import os


class Config:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    BOTS_FILE: str = os.getenv("BOTS_FILE")
