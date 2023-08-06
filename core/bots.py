"""This module contains the ChatBot and ChatBotLoom classes."""
import json
from jsonschema import validate

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


class ChatBot:
    """A representation of a chatbot, with metadata and an entrypoint."""

    def __init__(self, id, name, description, entrypoint):
        self.id = id
        self.name = name
        self.description = description
        self.entrypoint = entrypoint

    def __repr__(self):
        return f"<ChatBot id={self.id} name={self.name} description={self.description} entrypoint={self.entrypoint}>"

    def __str__(self):
        return f"{self.name} ({self.description})"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


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

    def get_bot(self, bot_id):
        """Returns a bot with the given id, or None if no bot is found."""
        for bot in self.bots:
            if bot.id == bot_id:
                return bot
        return None

    def get_bot_by_name(self, name):
        """Returns a bot with the given name, or None if no bot is found."""
        for bot in self.bots:
            if bot.name == name:
                return bot
        return None

    def load_bots_from_file(self, filename):
        """Loads bots from a JSON file."""
        with open(filename, "r", -1, "utf-8") as bots_file:
            bots = json.load(bots_file)
        validate(instance=bots, schema=BOTS_SCHEMA)
        self.bots = [
            ChatBot(bot["id"], bot["name"], bot["description"], bot["entrypoint"])
            for bot in bots
        ]

    def save_bots_to_file(self, filename):
        """Saves bots to a JSON file."""
        with open(filename, "w", -1, "utf-8") as bots_file:
            json.dump(
                [
                    {
                        "id": bot.id,
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
