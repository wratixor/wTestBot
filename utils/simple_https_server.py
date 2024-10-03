import asyncio
import logging

from aiohttp import web
import ssl

logger = logging.getLogger(__name__)

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def main():
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])

    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain('selfsigned.crt', 'selfsigned.key')
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 443, ssl_context=ssl_context)
    await site.start()
    try:
        while True:
            await asyncio.sleep(3600)
    except Exception as e:
        logger.error(f'main(): {e}')
    finally:
        await exit(0)

if __name__ == '__main__':
    asyncio.run(main())


