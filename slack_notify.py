import sys
from slack_utils.slack_client import send_slack_message

if __name__ == "__main__":
    status = sys.argv[1]
    if status == "passed":
        send_slack_message("All tests passed in CI pipeline!")
    else:
        send_slack_message("Test failures detected in CI pipeline!")