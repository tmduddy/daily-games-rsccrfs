import os
import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Edit me. Lowercased keys are what you type: `/daily-<key>`, `/daily <key>`, `@Daily Games <key>`.
GAMES = {
    "Krillion": "https://krillion.io/",
    "MapTap": "https://maptap.gg/",
    "CatFishing": "https://catfishing.net/",
}


def blocks(name):
    name = name.strip().lower()
    picks = [(n, url) for n, url in GAMES.items() if name in ("", n.lower())]
    if not picks:
        names = ", ".join(n.lower() for n in GAMES)
        return [{"type": "section", "text": {"type": "mrkdwn", "text": f"Don't know `{name}`. Try: {names}"}}]
    return [{"type": "section", "text": {"type": "mrkdwn", "text": f"Daily 🧵 for *<{url}|{n}>* [SPOILERS HOT]"}} for n, url in picks]


if __name__ == "__main__":
    app = App(token=os.environ["SLACK_BOT_TOKEN"])

    # Matches /daily (game in the text) and /daily-catfishing (game in the command name).
    @app.command(re.compile(r"^/daily"))
    def slash(ack, respond, command):
        ack()
        name = command["command"].removeprefix("/daily").lstrip("-") or command.get("text", "")
        respond(response_type="in_channel", blocks=blocks(name), text="Daily games", unfurl_links=False, unfurl_media=False)

    @app.event("app_mention")
    def mention(event, say):
        say(blocks=blocks(re.sub(r"<@\w+>", "", event["text"])), text="Daily games", unfurl_links=False, unfurl_media=False)

    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
