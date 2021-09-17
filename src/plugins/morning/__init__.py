# import nonebot
from nonebot import get_driver,on_message
from nonebot.plugin import on_startswith
from nonebot.adapters.cqhttp import Bot,GroupMessageEvent, event,Message
from requests import get
from .config import Config

global_config = get_driver().config
config = Config(**global_config.dict())

morn=on_startswith('早安')

@morn.handle()
async def morni(bot:Bot,event:GroupMessageEvent):
    imgurl = "https://api.xingzhige.com/API/zwimg/api.php"
    cqimg = f"[CQ:image,file=1.{imgurl.split('.')[1]},url={imgurl}]"
    await morn.finish(Message(cqimg))
# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass
