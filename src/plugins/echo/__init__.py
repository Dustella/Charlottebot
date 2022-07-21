from nonebot.adapters.onebot.v11 import MessageEvent, GroupMessageEvent, Bot, Message
from nonebot import on_command, on_message

echo = on_command('echo')


@echo.handle()
async def echow(bot: Bot, event: MessageEvent):
    await echo.finish(Message(str(event.get_message())[5:]))

xml_echo = on_message()

@xml_echo.handle()
async def lalal(bot: Bot, event: GroupMessageEvent):
    if not event.group_id == 1053741842:
        return
    eventjson = event.json()
    message_content = str(event.get_message())
    eventdict = json.loads(eventjson)
    mtype = eventdict['message'][0]['type']
    if mtype == 'xml':
        tsd = str(eventdict['message'][0]['data']['data'])
        await xml_echo.finish(message=tsd)
    elif mtype == 'text' and message_content.startswith('<?xml'):
        tsd = '[CQ:xml,data='+message_content+']'
        await bot.send_group_msg(group_id=event.group_id, message=tsd, auto_escape=False)
        await xml_echo.finish()