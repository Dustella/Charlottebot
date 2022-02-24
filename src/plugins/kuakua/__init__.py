from httpx import get
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Bot,MessageEvent

kuakua=on_keyword({"要夸夸","夸夸"})

@kuakua.handle()
async def kuakuaa(bot:Bot,event:MessageEvent):
    content=str(event.get_message())
    tsd=get(f"https://api.kuakua.dustella.net/getKuakua?sentence={content}").text
    await kuakua.finish(tsd)