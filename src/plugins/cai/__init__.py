from nonebot import on_message,on_command,on_startswith,on_keyword
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Event,Message,MessageEvent,GroupMessageEvent,PrivateMessageEvent

hyperspace=980330782
cai=on_keyword({"我好菜","真的菜","太菜了","真菜","我什么也不会"})
@cai.handle()
async def handle_cai(bot:Bot,event:GroupMessageEvent,state:T_State):
    if event.sender.user_id==732624987:
        await cai.finish("Dustella大菜狗！")
    else:
        await cai.finish("大佬谦虚啦！")

cai=on_keyword({"嘉然"})
@cai.handle()
async def handle_cai(bot:Bot,event:GroupMessageEvent,state:T_State):
    await cai.finish("嘉心糖给爷爬")