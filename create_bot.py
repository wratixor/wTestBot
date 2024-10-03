import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from db_handlers.db_class import PostgresHandler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#pg_db = PostgresHandler(config('PG_LINK'))
storage = RedisStorage.from_url(config('REDIS_LINK'))
scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
admins = set(int(admin_id) for admin_id in config('ADMINS').split(','))


bot = Bot(token=config('BOT_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)