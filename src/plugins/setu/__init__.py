from nonebot import on_command,on_keyword
from nonebot.adapters.cqhttp import Bot,Event,Message
from nonebot.typing import T_State
from random import randint
import httpx


setu = on_command('acgimage')

@setu.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    async with httpx.AsyncClient() as client:
        resp = await client.get('https://someacg.rocks/api/random?detail=1')
        imgurl = resp.json()["picUrl"]
        # get image Here

        cqimg = f"[CQ:image,file=1.{imgurl.split('.')[1]},url={imgurl}]"
        await setu.send(Message(cqimg))

cats=on_keyword({"猫猫来","猫来","猫再来"})

@cats.handle()
async def cat(bot:Bot,event:Event):
    async with httpx.AsyncClient() as client:
        resp = await client.get('https://api.thecatapi.com/v1/images/search')
        imgurl = resp.json()[0]["url"]
        # get image Here

        cqimg = f"[CQ:image,file=1.{imgurl.split('.')[1]},url={imgurl}]"
        await setu.send(Message(cqimg))