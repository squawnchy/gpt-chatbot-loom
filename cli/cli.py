"""The CLI for the chatbot loom."""
import os
import sys
import openai
import dotenv
from colorama import Fore, Style
from pyfiglet import Figlet
from core import ChatBotLoom, ChatBot, run_chat_ui


def prompt_user_for_choice(prompt, choices, to_display_text):
    """Prompts the user to select a choice from a list."""
    print(prompt)
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {to_display_text(choice)}")
    while True:
        try:
            choice = int(input("Enter a number: "))
            if choice > len(choices) or choice < 1:
                raise ValueError
            return choices[choice - 1]
        except ValueError:
            print("Invalid choice. Please enter a number.")


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
        print(Fore.GREEN + figlet.renderText("Chat Bot Loom CLI") + Style.RESET_ALL)

        # load bots from file if file exists
        if os.path.exists(file_path):
            loom.load_bots_from_file(file_path)
        else:
            loom.save_bots_to_file(file_path)

        # create a choice list for the bot names
        choices = []
        for bot in loom.bots:
            choices.append(bot)
        choices.append("Create a new bot")

        def get_display_name(bot_or_text):
            if isinstance(bot_or_text, ChatBot) and bot_or_text.name:
                return bot_or_text.name + " - " + bot_or_text.description
            return bot_or_text

        # prompt the user to select a bot
        selection = prompt_user_for_choice(
            "Select a bot to chat with or create a new bot", choices, get_display_name
        )

        # if the user selected to create a new bot, prompt them for a name
        if selection == "Create a new bot":
            print(Fore.YELLOW + "Creating a new bot..." + Style.RESET_ALL)
            selection = input("Enter a name for your bot: ")
            bot_description = input("Enter a description for your bot: ")
            bot_entrypoint = input("Enter a entrypoint for your bot: ")
            bot = ChatBot(selection, bot_description, bot_entrypoint)
            loom.add_bot(bot)
            loom.save_bots_to_file(file_path)
            sys.exit(0)
        else:
            print(Fore.YELLOW + f"Chatting with {selection.name}..." + Style.RESET_ALL)
            bot = loom.get_bot_by_name(selection.name)

        openai.api_key = os.getenv("OPENAI_API_KEY")
        # chat with the bot
        run_chat_ui(bot)
    except KeyboardInterrupt:
        print(Fore.RED + "\nExiting..." + Style.RESET_ALL)
        sys.exit(0)
    except Exception as unexpected_error:
        print(Fore.RED + f"Error: {unexpected_error}" + Style.RESET_ALL)
        sys.exit(1)
