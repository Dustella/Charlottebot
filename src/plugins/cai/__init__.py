from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent

hyperspace = 980330782
cai = on_keyword({"我好菜", "真的菜", "太菜了", "真菜", "我什么也不会"})


@cai.handle()
async def handle_cai(bot: Bot, event: GroupMessageEvent):
    if event.sender.user_id == 732624987:
        await cai.finish("Dustella大菜狗！")
    else:
        await cai.finish("大佬谦虚啦！")
