from nonebot import on_keyword
from nonebot.adapters.cqhttp import Bot,Event,Message
from nonebot.typing import T_State
from random import randint
import httpx


setu = on_keyword({"猫猫来"})

@setu.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    async with httpx.AsyncClient() as client:
        resp = await client.get('https://someacg.rocks/api/list?page=2').json()
        imgurl = resp["list"][randint(1,30)]["picUrl"]
        cqimg = f"[CQ:image,file=1.{imgurl.split('.')[1]},url={imgurl}]"
        await setu.send(Message(cqimg))

