from nonebot import on_startswith
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Event,Message,MessageEvent,GroupMessageEvent,PrivateMessageEvent
import json

auto=on_startswith({'.','。','~'})

@auto.handle()
async def autoi(bot:Bot,event:GroupMessageEvent):
    print('OK')
    args=str(event.get_message()).strip()
    print(args)
    if '[CQ:at' in args:
        print('OK')
        mjs=json.loads(event.json())['message']
        print(mjs)
        if len(mjs)==2:
            text=json.loads(event.json())['message'][0]['data']['text'].replace('.','')
            source_qq=event.sender.user_id
            target_qq=json.loads(event.json())['message'][1]['data']['qq']
            target_msg=f"[CQ:at,qq={source_qq}] {text}了[CQ:at,qq={target_qq}]！~"
            await auto.finish(Message(target_msg))
        elif len(mjs)==3:
            text1=json.loads(event.json())['message'][0]['data']['text'].replace('.','')
            text2=json.loads(event.json())['message'][2]['data']['text']
            source_qq=event.sender.user_id
            target_qq=json.loads(event.json())['message'][1]['data']['qq']
            target_msg=f"[CQ:at,qq={source_qq}] {text1} [CQ:at,qq={target_qq}] {text2}！~"
            await auto.finish(Message(target_msg))
        else:
            await auto.finish("啦啦啦？")