from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot.log import logger
from requests import get



whois = on_command('whois')


@whois.handle()
async def ping_ip(bot: Bot, event: MessageEvent):
    args = str(event.get_message()).split(' ')[1]
    try:
        response_ping = get(url=f"https://api.ooii.io/ping?host={args}").json()
        logger.info(response_ping)
        tosend = f"""
域名：{response_ping["host"]}
ip: {response_ping["ip"]}
地点: {response_ping["location"]}
        """
        logger.info(tosend)
        await whois.finish(tosend)
    except Exception as e:
        await whois.finish(str(e))
