from nonebot import on_keyword
from nonebot.adapters.cqhttp import Bot,Event,Message
from nonebot.typing import T_State
import httpx


setu = on_keyword({"涩图来","色图来"})

@setu.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    async with httpx.AsyncClient() as client:
        resp = await client.get('https://api.nyan.xyz/httpapi/sexphoto')
        imgurl = resp.json()['data']['url'][0]
        cqimg = f"[CQ:image,file=1.{imgurl.split('.')[1]},url={imgurl}]"
        await setu.send(Message(cqimg))

