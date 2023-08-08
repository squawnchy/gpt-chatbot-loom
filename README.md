# gpt-chatbot-loom

## Description

"gpt-chatbot-loom" is a tool for creating various "figures" or "characters". These bots enhance the user experience through a local web interface, which is personalized by the name and function of the bots.

## Technologies

The project uses Python as the primary programming language and integrates the use of ChatGPT for bot creations and gradio for the web interface.

## Project Status

The project has just started. It's functional but still in its infancy.

## Installation & Usage

The tool can be run using Python:

```bash
python -m pip install -r requirements.txt
python -m chatbot_loom
```

You can do it the easy way by running the following script:

```bash
./run.sh
```

### Features

The tool allows for the creation and usage of chatbots:

- **Creating Chatbots** - Bot creation is currently done manually by depositing a JSON file, which has to follow a certain schema. The path to this file is determined by the `BOTS_FILE` environment variable. If no file is found, a standard bot file is automatically created.
  The schema looks like this:

```
{
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
```

- **Using Chatbots** - Chatbots are used via a web interface, where bots can be selected via tabs. To use the bots, an API key for OpenAI must be deposited via the `OPENAI_API_KEY` environment variable.

![Screenshot](/assets/screenshot_01.png)

## Contribution

Want to contribute? Just create a pull request.

## License

[GNU GENERAL PUBLIC LICENSE](https://github.com/squawnchy/gpt-chatbot-loom/blob/main/LICENSE)
