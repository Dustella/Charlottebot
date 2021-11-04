from types import CodeType
from nonebot.adapters.cqhttp import Bot, MessageEvent, event
from nonebot.adapters.cqhttp.message import Message
from nonebot import on_command


beast = ['啦', 'la', '！', '~']


def str2hex(text: str):
    ret = ""
    for x in text:
        charHexStr = hex(ord(x))[2:]
        if len(charHexStr) == 3:
            charHexStr = "0" + charHexStr
        elif len(charHexStr) == 2:
            charHexStr = "00" + charHexStr
        ret += charHexStr
    return ret


def hex2str(text: str):
    ret = ""
    for i in range(0, len(text), 4):
        unicodeHexStr = text[i:i + 4]
        charStr = chr(int(unicodeHexStr, 16))
        ret += charStr
    return ret


def wencode(str):
    hexArray = list(str2hex(str))
    code = ""
    n = 0
    for x in hexArray:
        k = int(x, 16) + n % 16
        if k >= 16:
            k -= 16
        code += beast[int(k / 4)] + beast[k % 4]
        n += 1
    return code


def wdecode(str):
    hexArray = list(str)
    code = ""
    for i in range(0, len(hexArray), 2):
        pos1 = beast.index(hexArray[i])
        pos2 = beast.index(hexArray[i + 1])
        k = ((pos1 * 4) + pos2) - (int(i / 2) % 16)
        if k < 0:
            k += 16
        code += hex(k)[2:]
    return hex2str(code)


dec=on_command('la')

@dec.handle()
async def decode(bot:Bot,event:MessageEvent):
    print(str(event.get_message()))
    winput=str(event.get_message())
    result=wdecode(winput)
    tsend=Message(str(result))
    await dec.finish(tsend)

enc=on_command('lla')

@enc.handle()
async def encode(bot:Bot,event=MessageEvent):
    einput=str(event.get_message())
    result=wencode(einput)
    print(result)
    tsend=Message(str(result))
    await enc.finish(tsend)
    