"""This module contains the ChatBot and ChatBotLoom classes."""
import json
from uuid import uuid4
from jsonschema import validate
from openai import ChatCompletion

BOTS_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "description": {"type": "string"},
            "entrypoint": {"type": "string"},
        },
        "required": ["id", "name", "description", "entrypoint"],
    },
}

CHAT_GPT_MODEL_ID = "gpt-4"


class ChatBot:
    """A representation of a chatbot, with metadata and an entrypoint."""

    def __init__(self, name, description, entrypoint):
        self.identifier = uuid4().hex
        self.name = name
        self.description = description
        self.entrypoint = entrypoint

    def __repr__(self):
        return f"<ChatBot id={self.identifier} name={self.name} description={self.description}>"

    def __str__(self):
        return f"{self.name} ({self.description})"

    def __eq__(self, other):
        if not isinstance(other, ChatBot):
            return False
        return self.identifier == other.id

    def __hash__(self):
        return hash(self.identifier)

    def _initialize_chat(self):
        """Initializes a chat with the chatbot."""
        return [{"role": "system", "content": self.entrypoint}]

    def chat(self, message, plain_history: list[list[str, str]]):
        """Sends a message to the chatbot and returns the response."""

        message_history = self._initialize_chat()
        for message_tuple in plain_history:
            message_history.append({"role": "user", "content": message_tuple[0]})
            message_history.append({"role": "system", "content": message_tuple[1]})
        message_history.append({"role": "user", "content": message})

        response = ChatCompletion.create(
            model=CHAT_GPT_MODEL_ID,
            messages=message_history,
        )
        response_message = response["choices"][0]["message"]["content"]
        return response_message


class ChatBotLoom:
    """A collection of chatbots, their metadata and functions to load and save them."""

    def __init__(self, bots: list[ChatBot] = None):
        if bots is None:
            bots = []
        self.bots = bots

    def __repr__(self):
        return f"<ChatBotLoom bots={self.bots}>"

    def __str__(self):
        return f"{self.bots}"

    def __eq__(self, other):
        return self.bots == other.bots

    def __hash__(self):
        return hash(self.bots)

    def _find_bot(self, criteria, value):
        """Helper method to find a bot based on a given criteria."""
        for bot in self.bots:
            if getattr(bot, criteria) == value:
                return bot
        return None

    def get_bot(self, bot_id):
        """Returns a bot with the given id, or None if no bot is found."""
        return self._find_bot("identifier", bot_id)

    def get_bot_by_name(self, name):
        """Returns a bot with the given name, or None if no bot is found."""
        return self._find_bot("name", name)

    def load_bots_from_file(self, filename):
        """Loads bots from a JSON file."""
        with open(filename, "r", -1, "utf-8") as bots_file:
            bots = json.load(bots_file)
        validate(instance=bots, schema=BOTS_SCHEMA)
        self.bots = [
            ChatBot(bot["name"], bot["description"], bot["entrypoint"]) for bot in bots
        ]

    def save_bots_to_file(self, filename):
        """Saves bots to a JSON file."""
        with open(filename, "w", -1, "utf-8") as bots_file:
            json.dump(
                [
                    {
                        "id": bot.identifier,
                        "name": bot.name,
                        "description": bot.description,
                        "entrypoint": bot.entrypoint,
                    }
                    for bot in self.bots
                ],
                bots_file,
                indent=4,
            )

    def add_bot(self, bot: ChatBot):
        """Adds a bot to the list of bots."""
        self.bots.append(bot)

    def remove_bot(self, bot: ChatBot):
        """Removes a bot from the list of bots."""
        self.bots.remove(bot)

    def create_sample_bot(self):
        """
        Creates a sample bot with a predefined structure 
        and adds it to the bot collection.
        """

        example_bot_json_structure = {
            "name": "MindGuru",
            "description": "A calming presence that can offer advice, encouragement, "
            "and mindfulness tips",
            "entrypoint": (
                "You are MindGuru, my personal psychology bot. "
                "You are a calming presence who can offer advice, encouragement, "
                "and tips for mindfulness. You are empathetic and always willing to "
                "help me cope with stress."
            )
        }

        sample_bot_description = (
            "A sample bot for creating new bots, that you can add to your "
            "collection of bots."
        )

        sample_bot_entrypoint = (
            f"You are a chatbot for creating other chatbots in an application. "
            f"Your task is to explain to the user how to create a new chatbot by "
            f"writing the JSON structure into the file. Provide them with a JSON "
            f"structure they can use to create a new chatbot. This program saves bots "
            f"and validates them using the following JSON schema: {BOTS_SCHEMA}. "
            f"A bot could look like this: {example_bot_json_structure}. "
            f"Note that 'entrypoint' is a prompt for ChatGPT telling it how to act. "
            f"It's not a message the user will see."
        )

        sample_bot = ChatBot("Chatbot Loom", sample_bot_description, sample_bot_entrypoint)

        self.add_bot(sample_bot)

        return sample_bot
