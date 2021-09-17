from aiohttp import ClientSession


async def get_weather_of_city(city: str) -> str:
    #API地址
    url = 'https://www.tianqiapi.com/api'
    #请求参数
    payload = '?version=v61&appid=18563822&appsecret=eziD3wIu&city='+city
    
    async with ClientSession() as sess:
        async with sess.post(url+payload) as response:
            res_payload = await response.json()
            # print(res_payload)
            date = str(res_payload['date']).split(sep='-')
            res = f"今天是{date[0]}年{date[1]}月{date[2]}号,{res_payload['week']}\n" +\
                  f"{res_payload['city']}天气：{res_payload['wea']}\n当前温度：{res_payload['tem']}°\n" +\
                  f"{res_payload['air_tips']}\n" +\
                  f"上次天气更新时间：{res_payload['update_time']}"

    return res