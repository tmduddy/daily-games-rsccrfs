# daily-games-rsccrfs
daily games slack app

## Setup
1. api.slack.com/apps -> your app -> **App Manifest**: paste `manifest.yml`, save.
2. **Basic Information -> App-Level Tokens**: create one with `connections:write` -> `SLACK_APP_TOKEN` (`xapp-...`).
3. **Install App** -> copy Bot User OAuth Token -> `SLACK_BOT_TOKEN` (`xoxb-...`). Reinstall after manifest changes.
4. Run:
   ```
   python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
   SLACK_BOT_TOKEN=xoxb-... SLACK_APP_TOKEN=xapp-... .venv/bin/python app.py
   ```
5. `/invite @Daily Games` in a channel to use @-mentions (slash commands work anywhere).

## Adding a game
Add it to `GAMES` in `app.py`. For a `/daily-<name>` shortcut, also add it to `manifest.yml` and re-paste.
