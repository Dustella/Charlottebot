from nonebot.adapters.onebot.v11 import MessageEvent, Bot, Message
from nonebot import on_command

echo = on_command('echo')


@echo.handle()
async def echow(bot: Bot, event: MessageEvent):
    await echo.finish(Message(str(event.get_message())[5:]))
