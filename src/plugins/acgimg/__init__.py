from nonebot import on_command, on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event, Message
from requests import get
from random import randint

acgimg = on_keyword({"来点色色", "来点涩涩", "我想色色", "我想涩涩",
                    "色图来", "瑟图来", "涩图来", "来点瑟瑟"})
acgimg_command = on_command("acgimage")


@acgimg_command.handle()
@acgimg.handle()
async def cat(bot: Bot, event: Event):
    url = get('https://acg-img.dustella.net/api').json()["url"]
    cqimg = f"[CQ:image,file=1.{url.split('.')[1]},url={url}]"
    await acgimg.send(Message(cqimg))
