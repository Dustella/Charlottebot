from dataclasses import FrozenInstanceError
from nonebot.adapters.cqhttp import Bot, MessageEvent
from nonebot import on_command

calc=on_command('calc')

@calc.handle()
async def claaa(bot:Bot,event:MessageEvent):
    ban_list={"os","import","open","delete","__"}
    if str(event.get_message()) in ban_list: calc.finish()
    args=str(event.get_message()).strip()
    try:
        result=eval(args)
    except:
        result='Bad Expression'
    print(str(result))
    result=str(result)
    await calc.finish(result)