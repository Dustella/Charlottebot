from nonebot import get_driver,on_command
from nonebot.adapters.cqhttp import Bot,MessageEvent
from .config import Config

global_config = get_driver().config
config = Config(**global_config.dict())

help=on_command('help')

@help.handle()
async def help(bot:Bot, message:MessageEvent):
    help_text="""
    commands:
    /help: get help for bot
    /ao: decode beast encoding
    /wu: encode beast encoding
    /enc: encode base64
    /dec: decode base64
    /calc: calculate an expression
    /acgimage: gives an acg image
    /echo: echo the message
    keywords:
    我好菜啊
    .[操作]@人
    猫猫来
    """
    await help.finish(help_text)