from dataclasses import FrozenInstanceError
from nonebot.adapters.cqhttp import Bot, MessageEvent
from nonebot import on_command

calc=on_command('calc')

@calc.handle()
async def claaa(bot:Bot,event:MessageEvent):
    if 'os' in event.get_message():return
    if 'import' in event.get_message():return
    args=str(event.get_message()).strip()
    try:
        result=eval(args)
    except:
        result='Bad Expression'
    print(str(result))
    result=str(result)
    await calc.finish(result)