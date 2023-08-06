"""The CLI for the chatbot loom."""
import os
import openai
from core import ChatBotLoom, ChatBot, Config, run_chat_ui


def prompt_user_for_choice(prompt, choices):
    """Prompts the user to select a choice from a list."""
    print(prompt)
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")
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
    config = Config()
    openai.api_key = config.OPENAI_API_KEY

    loom = ChatBotLoom()
    # load bots from file if file exists
    if os.path.exists(config.BOTS_FILE):
        loom.load_bots_from_file(config.BOTS_FILE)
    else:
        loom.save_bots_to_file(config.BOTS_FILE)

    # create a choice list for the bot names
    bot_names = [bot.name for bot in loom.bots]
    bot_names.append("Create a new bot")

    # prompt the user to select a bot
    bot_name = prompt_user_for_choice(
        "Select a bot to chat with or create a new bot", bot_names
    )

    # if the user selected to create a new bot, prompt them for a name
    if bot_name == "Create a new bot":
        bot_name = input("Enter a name for your bot: ")
        bot_description = input("Enter a description for your bot: ")
        bot_entrypoint = input("Enter a entrypoint for your bot: ")
        bot = ChatBot(bot_name, bot_description, bot_entrypoint)
    else:
        bot = loom.get_bot(bot_name)

    # chat with the bot
    run_chat_ui(bot)
