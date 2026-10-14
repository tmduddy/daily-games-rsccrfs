import os
import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Edit me. Keys are what you type: `/daily-<key>`, `/daily <key>`, `@Daily Games <key>`.
GAMES = {
    "wordle": "https://www.nytimes.com/games/wordle/index.html",
    "connections": "https://www.nytimes.com/games/connections",
    "strands": "https://www.nytimes.com/games/strands",
    "mini": "https://www.nytimes.com/crosswords/game/mini",
    "catfishing": "https://catfishing.net",
    "framed": "https://framed.wtf",
}


def blocks(name):
    name = name.strip().lower()
    if name and name not in GAMES:
        return [{"type": "section", "text": {"type": "mrkdwn", "text": f"Don't know `{name}`. Try: {', '.join(GAMES)}"}}]
    picks = {name: GAMES[name]} if name else GAMES
    return [{"type": "section", "text": {"type": "mrkdwn", "text": f"*<{url}|{n.title()}>*"}} for n, url in picks.items()]


if __name__ == "__main__":
    app = App(token=os.environ["SLACK_BOT_TOKEN"])

    # Matches /daily (game in the text) and /daily-catfishing (game in the command name).
    @app.command(re.compile(r"^/daily"))
    def slash(ack, respond, command):
        ack()
        name = command["command"].removeprefix("/daily").lstrip("-") or command.get("text", "")
        respond(response_type="in_channel", blocks=blocks(name), text="Daily games")

    @app.event("app_mention")
    def mention(event, say):
        say(blocks=blocks(re.sub(r"<@\w+>", "", event["text"])), text="Daily games")

    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
