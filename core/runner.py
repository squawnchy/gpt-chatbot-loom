"""Runs UI for interacting with a chatbot."""
import gradio as gr
from .bots import ChatBot


def create_chatbot_ui(bot: ChatBot):
    """Creates a UI for the given chatbot."""

    def chat(message, history):
        return bot.chat(message)

    return gr.ChatInterface(
        fn=chat,
        textbox=gr.Textbox(lines=5, placeholder="Type your message here..."),
        retry_btn=None,
        stop_btn=None,
        undo_btn=None,
        clear_btn=None,
        title=bot.name,
        description=bot.description,
        chatbot=gr.Chatbot(height=480),
    )


def run_chat_ui(bot: ChatBot):
    """Runs the UI for the given chatbot."""
    chat_ui = create_chatbot_ui(bot)
    chat_ui.launch()


def run_tabbed_chat_ui(chatbots: list[ChatBot]):
    """Runs the UI for the given chatbot."""

    gr.TabbedInterface(
        interface_list=[create_chatbot_ui(bot) for bot in chatbots],
        tab_names=[bot.name for bot in chatbots],
    ).launch()
