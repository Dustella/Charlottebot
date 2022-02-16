from nonebot import on_startswith
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent
from nonebot.log import logger
import json

auto = on_startswith({'.', '。', '~'})


@auto.handle()
async def autoi(bot: Bot, event: GroupMessageEvent):
    args = str(event.get_message()).strip()

    msgJson = json.loads(event.json())['message']

    text = json.loads(event.json())['message'][0]['data']['text'].replace(
        '.', '').replace('。', '')
    text2 = ''

    source_qq = event.sender.user_id
    if event.reply:
        target_qq = event.reply.sender.user_id
    else:
        target_qq = json.loads(event.json())['message'][1]['data']['qq']

    if len(msgJson) == 3:
        text2 = json.loads(event.json())['message'][2]['data']['text']
    elif len(msgJson) == 1 or len(msgJson) == 2:
        pass
    else:
        await auto.finish("啦啦啦？")

    target_msg = assembleMsg(text, text2, source_qq, target_qq)
    await auto.finish(target_msg)


def assembleMsg(text1: str, text2: str, source_qq: str, target_qq: str) -> Message:
    target_msg = f"[CQ:at,qq={source_qq}] {text1} [CQ:at,qq={target_qq}] {text2}！~"
    return Message(target_msg)
