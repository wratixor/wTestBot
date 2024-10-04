import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
#from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler

#storage = RedisStorage.from_url(config('REDIS_LINK_0'))
storage = MemoryStorage()

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
admins = set(int(admin_id) for admin_id in config('ADMINS').split(','))

bot = Bot(token=config('BOT_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)