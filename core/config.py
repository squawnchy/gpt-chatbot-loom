"""config module."""
import os


class Config:
    """config set from environment variables."""

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    BOTS_FILE: str = os.getenv("BOTS_FILE")
