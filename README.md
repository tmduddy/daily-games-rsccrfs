# daily-games-rsccrfs
daily games slack app

## Setup
1. api.slack.com/apps -> your app -> **App Manifest**: paste `manifest.yml`, save.
2. **Basic Information -> App-Level Tokens**: create one with `connections:write` -> `SLACK_APP_TOKEN` (`xapp-...`) in `.env`.
3. **Install App** -> copy Bot User OAuth Token -> `SLACK_BOT_TOKEN` (`xoxb-...`) in `.env`. Reinstall after manifest changes.
4. Run:
   ```
   python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
   set -a && . ./.env && set +a && .venv/bin/python app.py
   ```
5. `/invite @Daily Games` in a channel to use @-mentions (slash commands work anywhere).

## Adding a game
Add it to `GAMES` in `app.py`. For a `/daily-<name>` shortcut, also add it to `manifest.yml` and re-paste.

## Running on the Pi (Portainer)
Socket Mode only makes outbound connections, so the Pi doesn't need to be reachable from the internet.

1. Portainer -> **Stacks** -> **Add stack** -> **Repository**.
   - URL: this repo. Private repo -> enable **Authentication** with a GitHub fine-grained PAT (read-only Contents on this repo).
   - Compose path: `docker-compose.yml`.
2. **Environment variables**: add `SLACK_BOT_TOKEN` and `SLACK_APP_TOKEN`.
3. Deploy. Logs are in the container's **Logs** view. Optionally enable **GitOps updates** so pushes to `main` redeploy.

Run only one copy long-term (stop the local one: `docker compose down`).
