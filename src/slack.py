import os

from slack_sdk import WebClient
from slack_sdk.models.blocks import (
    ContextBlock,
    TextObject,
    SectionBlock,
    ImageElement,
)

CLIENT = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
CHANNEL = "#sebix"

CLIENT.chat_postMessage(
    channel=CHANNEL,
    blocks=[
        ContextBlock(
            elements=[
                TextObject(type="mrkdwn", text=":tn: A NEW DROP!")
            ]
        ),
        SectionBlock(
            text=TextObject(
                type="mrkdwn",
                text="*Nike Air Max Plus*\n:dollar: 879,99 zł\n https://www.nike.com/pl/t/buty-meskie-air-max-plus-P39sRg/DZ4507-600"
            ),
            accessory=ImageElement(
                image_url="https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/c721f04c-9b3d-4eb8-95f8-5e7d36579345/buty-meskie-air-max-plus-P39sRg.png",
                alt_text="Nike Air Max Plus"
            )
        )
    ]
)
