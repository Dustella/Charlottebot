from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot import on_command

calc = on_command('calc')

@calc.handle()
async def claaa(bot: Bot, event: MessageEvent):
    ban_list = {"os", "import", "open", "delete", "__","eval"}
    for i in ban_list:
        if i in str(event.get_message()):
            await calc.finish("dangourous expression")
    # handle dangourous situations
    
    args = str(event.get_message()).strip()
    try:
        result = eval(args)
    except:
        result = 'Bad Expression'
    # eval expression

    result = str(result)
    await calc.finish(result)
    # send