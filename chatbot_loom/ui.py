"""Runs UI for interacting with a chatbot."""
import gradio as gr
from .bots import ChatBotLoom, ChatBot


def create_chatbot_ui(bot: ChatBot):
    """Creates a UI for the given chatbot."""

    def chat(message, history):
        history = history or []
        response = bot.chat(message, history)
        return response

    chat_interface = gr.ChatInterface(
        fn=chat,
        textbox=gr.Textbox(lines=5, placeholder="Type your message here..."),
        retry_btn=None,
        stop_btn=None,
        title=bot.name,
        description=bot.description,
        chatbot=gr.Chatbot(height=400),
    )

    return chat_interface


def run_chat_ui(bot: ChatBot):
    """Runs the UI for the given chatbot."""
    chat_ui = create_chatbot_ui(bot)
    chat_ui.launch()


def run_tabbed_chat_ui(loom: ChatBotLoom):
    """Runs the UI for the given chatbot."""

    chatbots = loom.load_bots()
    gr.TabbedInterface(
        interface_list=[create_chatbot_ui(bot) for bot in chatbots],
        tab_names=[bot.name for bot in chatbots],
    ).launch(server_port=8967)
