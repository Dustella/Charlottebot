from nonebot import on_command, on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event, Message
import httpx
from random import randint

acgimg = on_keyword({"来点色色", "来点涩涩", "我想色色", "我想涩涩",
                    "色图来", "瑟图来", "涩图来", "来点瑟瑟"})
acgimg_command = on_command("acgimage")

@acgimg_command.handle()
@acgimg.handle()
async def cat(bot: Bot, event: Event):
    async with httpx.AsyncClient() as client:
        list = (await client.get(f'https://someacg.rocks/api/list?page={randint(1, 25)}')).json()["body"]
        imgurl = "https://cdn.someacg.rocks/images/" + \
            list[(randint(0, 29))]["file_name"]
        cqimg = f"[CQ:image,file=1.{imgurl.split('.')[1]},url={imgurl}]"
        await acgimg.send(Message(cqimg))
