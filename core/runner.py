"""Runs UI for interacting with a chatbot."""
import gradio as gr
from .bots import ChatBot


def run_chat_ui(bot: ChatBot):
    """Runs the UI for the given chatbot."""

    def chat(message, history):
        return bot.chat(message)

    gr.ChatInterface(
        fn=chat,
        textbox=gr.Textbox(lines=5, placeholder="Type your message here..."),
        retry_btn=None,
        stop_btn=None,
        undo_btn=None,
        clear_btn=None,
        title=bot.name,
        description=bot.description,
        chatbot=gr.Chatbot(height=480),
    ).launch()
