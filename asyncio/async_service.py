import asyncio
import json
from aiohttp import ClientSession, web


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            try:
                return f'{city}: {weather_json["weather"][0]["main"]}'
            except KeyError:
                return 'Нет данных'
            

async def handle(request):
    city = request.rel_url.query['city']
    weather = await get_weather(city)
    result = {'city': city, 'weather': weather}

    return web.Response(text=json.dumps(result, ensure_ascii=False))


async def main():
    app = web.Application()
    app.add_routes([web.get('/weather', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    while True:
        await asyncio.sleep(3600)


if __name__ == '__main__':
    asyncio.run(main())