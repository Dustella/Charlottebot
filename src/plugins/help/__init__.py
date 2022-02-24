from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent

help = on_command('help')


@help.handle()
async def help_text(bot: Bot, event: MessageEvent):
    help_text = """
    /help: 得到一些帮助
    /echo: 原样输出消息
    /whois: 查找 whois 信息
    我好菜啊
    .[操作]@人
    猫猫来
    """
    await help.finish(help_text)
