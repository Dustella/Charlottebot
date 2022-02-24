from nonebot import on_message
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot
import json

xmll = on_message()

@xmll.handle()
async def lalal(bot: Bot, event: GroupMessageEvent):
    if event.group_id == 1053741842:
        eventjson = event.json()
        message_content = str(event.get_message())
        eventdict = json.loads(eventjson)
        mtype = eventdict['message'][0]['type']
        if mtype == 'xml':
            tsd = str(eventdict['message'][0]['data']['data'])
            await xmll.finish(message=tsd)
        elif mtype == 'text' and message_content.startswith('<?xml'):
            tsd = '[CQ:xml,data='+message_content+']'
            await bot.send_group_msg(group_id=event.group_id, message=tsd, auto_escape=False)
            await xmll.finish()
