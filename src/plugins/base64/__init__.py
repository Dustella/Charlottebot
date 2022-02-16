from nonebot.adapters.onebot.v11 import Bot, MessageEvent, event
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command
from base64 import b64decode, b64encode

dec = on_command('dec')


@dec.handle()
async def decode(bot: Bot, event: MessageEvent):
    winput = str(event.get_message()).encode(encoding='utf-8')
    result = b64decode(winput)
    tsend = Message(str(result.decode(encoding='utf-8')))
    await dec.finish(tsend)

enc = on_command('enc')


@enc.handle()
async def encode(bot: Bot, event=MessageEvent):
    einput = str(event.get_message()).encode()
    result = b64encode(einput)
    tsend = Message(str(result.decode()))
    await enc.finish(tsend)
