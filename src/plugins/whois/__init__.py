from nonebot import get_driver, on_command
from nonebot.adapters.cqhttp import Bot, MessageEvent
from .config import Config
from requests import get
import json

global_config = get_driver().config
config = Config(**global_config.dict())

whois = on_command('whois')


@whois.handle()
async def ping_ip(bot: Bot, event: MessageEvent):
    req_ping = {"host": str(event.message)}
    req_icp={"domain":str(event.message)}
    try:
        response_ping = get(url="https://api.ooii.io/whois", params=req_ping).json()
        if response_ping['state'] == 1001:
            await whois.finish("域名错误")
        response_icp=get(url="https://api.ooii.io/beian/api.php",params=req_icp).json()
        tosend = f"""
域名：{response_ping["host"]}
ip: {response_ping["ip"]}
地点: {response_ping["location"]}
备案单位：{response_icp["unitName"]}
ICP：{response_icp["icp"]}
        """
        await whois.finish(tosend)
    except Exception as e:
        await whois.finish(str(e))
