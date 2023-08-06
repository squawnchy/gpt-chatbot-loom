"""Runs UI for interacting with a chatbot."""
import gradio as gr
from .bots import ChatBot


def run_chat_ui(bot: ChatBot):
    """Runs the UI for the given chatbot."""
    gr.ChatInterface(bot.chat).launch()
