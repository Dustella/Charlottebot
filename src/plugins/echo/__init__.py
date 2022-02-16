from nonebot.adapters.onebot.v11 import MessageEvent, Bot
from nonebot import on_command

echo = on_command('echo')


@echo.handle()
async def echow(bot: Bot, event: MessageEvent):
    await echo.finish(event.get_message())
