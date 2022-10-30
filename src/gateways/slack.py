import os

from slack_sdk import WebClient
from slack_sdk.models.blocks import (
    TextObject,
    SectionBlock,
)

from src.logger import get_logger
from src.models import NikeSearchResult

CLIENT = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
CHANNEL = "#sebix"

logger = get_logger("slack")


def notify_about_new_release(search_result: NikeSearchResult) -> None:
    try:
        CLIENT.chat_postMessage(
            channel=CHANNEL,
            blocks=[
                SectionBlock(
                    text=TextObject(type="mrkdwn", text=f":tn: *{search_result.name}*\n:dollar: {search_result.price}\n {search_result.url}"),
                )
            ]
        )
    except Exception as e:
        logger.error(e)
