import asyncio
import os

from django.conf import settings
from EnglishWeb import settings as default_settings

import django
import websockets

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EnglishWeb.settings')
settings.configure(default_settings, DEBUG=True)
django.setup()

from sesame.utils import get_user


async def handler(websocket):
    sesame = await websocket.recv()
    user = await asyncio.to_thread(get_user, sesame)
    if user is None:
        await websocket.close(1011, 'authentication failed')
        return

    await websocket.send(f'Hello {user}!')


async def main():
    async with websockets.serve(handler, 'localhost', 8000):
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
