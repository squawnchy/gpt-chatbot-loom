"""The CLI for the chatbot loom."""
import os
import sys
import openai
import dotenv
from colorama import Fore, Style
from pyfiglet import Figlet
from core import ChatBotLoom, run_tabbed_chat_ui


def run():
    """Runs the CLI."""

    try:
        # load .env file from one directory up
        dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
        dotenv.load_dotenv(dotenv_path)
        file_path = os.getenv("BOTS_FILE")
        loom = ChatBotLoom()

        # Add some color and ASCII Art
        figlet = Figlet(font="digital")
        print(Fore.GREEN + figlet.renderText("Chat Bot Loom") + Style.RESET_ALL)

        # load bots from file if file exists
        if os.path.exists(file_path):
            print(Fore.GREEN + f"Loading bots from {file_path}" + Style.RESET_ALL)
            loom.load_bots_from_file(file_path)
        else:
            print(Fore.YELLOW + f"No bots found at {file_path}" + Style.RESET_ALL)
            print(Fore.YELLOW + "Creating new bots file..." + Style.RESET_ALL)
            # create sample bot for creating new bots
            loom.create_sample_bot()
            loom.save_bots_to_file(file_path)

        openai.api_key = os.getenv("OPENAI_API_KEY")
        # chat with the bot
        run_tabbed_chat_ui(loom.bots)
    except KeyboardInterrupt:
        print(Fore.RED + "\nExiting..." + Style.RESET_ALL)
        sys.exit(0)
    except Exception as unexpected_error:  # pylint: disable=broad-exception-caught
        print(Fore.RED + f"Error: {unexpected_error}" + Style.RESET_ALL)
        sys.exit(1)
