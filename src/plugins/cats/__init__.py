from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event, Message
import httpx
from requests import get

cats = on_keyword({"猫猫来", "猫来", "猫再来"})


@cats.handle()
async def cat(bot: Bot, event: Event):
    async with httpx.AsyncClient() as client:
        resp = await client.get('https://api.thecatapi.com/v1/images/search')
        imgurl = resp.json()[0]["url"]

        cqimg = f"[CQ:image,file=1.{imgurl.split('.')[1]},url={imgurl}]"
        await cats.send(Message(cqimg))

cat_girl = on_keyword({"猫娘来", "来点猫娘"})


@cat_girl.handle()
async def cat_g(bot: Bot, event: Event):
    resp = get('https://acg-img.dustella.net/cats')
    location = resp.json()["url"]
    print(location)
    image = f"[CQ:image,file=1.{location.split('.')[1]},url={location}]"
    await cat_girl.finish(Message(image))
