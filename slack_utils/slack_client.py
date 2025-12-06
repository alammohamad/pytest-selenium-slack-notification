# import requests
# import yaml
#
# def load_webhook():
#     with open("config/settings.yaml") as f:
#         data = yaml.safe_load(f)
#     return data["slack_webhook"]
#
# def send_slack_message(message):
#     webhook = load_webhook()
#     payload = {"text": message}
#     print(f"Sending Slack message: {message}")  # <-- debug
#     response = requests.post(webhook, json=payload)
#     print(f"Response status: {response.status_code}, {response.text}")
# ### still good for test and get slack notification

##-----------updating for github, below codes
# import os
# import requests
# import yaml
# from pathlib import Path
#
# def load_webhook():
#     # First, try env variable
# 
#     if webhook:
#         return webhook
#
#     # Fallback to local config file
#     path = Path("config/settings.yaml")
#     with path.open() as f:
#         data = yaml.safe_load(f)
#     return data["slack_webhook"]
import os
import requests
import yaml
from pathlib import Path

def load_webhook():
    webhook = os.environ.get("SLACK_WEBHOOK_URL")
    if webhook:
        return webhook

    path = Path("config/settings.yaml")
    with path.open() as f:
        data = yaml.safe_load(f)

    return data.get("slack_webhook", "REPLACE_ME")

def send_slack_message(message):
    webhook = load_webhook()
    payload = {"text": message}
    print(f"Sending Slack message: {message}")
    response = requests.post(webhook, json=payload)
    print(f"Response status: {response.status_code}, {response.text}")