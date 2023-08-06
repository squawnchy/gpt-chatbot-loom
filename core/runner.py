"""Runs UI for interacting with a chatbot."""
import openai
import gradio as gr
from .bots import ChatBot
from .config import Config


def run_ui(bot: ChatBot):
    """Runs the UI for the given chatbot."""

    config = Config()
    openai.api_key = config.OPENAI_API_KEY
    gr.ChatInterface(bot.chat).launch()
