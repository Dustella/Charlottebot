from nonebot import get_driver, on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from .config import Config

global_config = get_driver().config
config = Config(**global_config.dict())

help = on_command('help')


@help.handle()
async def help_text(bot: Bot, event: MessageEvent):
    help_text = """
    commands:
    /help: get help for bot\
    /enc: encode base64
    /dec: decode base64
    /calc: calculate an expression
    /echo: echo the message
    /whois [domain]: get whois information
    keywords:
    我好菜啊
    .[操作]@人
    猫猫来
    早安
    """
    await help.finish(help_text)
