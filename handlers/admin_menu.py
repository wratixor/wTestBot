import logging
from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, ReplyKeyboardRemove

from create_bot import admins, dp, bot
from filters.is_admin import IsAdmin
from keyboards.all_kb import admin_kb, private_kb, main_kb

logger = logging.getLogger(__name__)
admin_router = Router()

@admin_router.message(F.text == '⚙️ Админка', IsAdmin(admins))
async def get_admin_kb(message: Message):
    await message.answer('Привет, админ!', reply_markup=admin_kb())

@admin_router.message(F.text == '🔙 Назад', IsAdmin(admins))
async def get_admin_kb(message: Message):
    if message.chat.type == 'private':
        kb=private_kb(message.from_user.id)
    else:
        kb=main_kb(message.from_user.id)
    await message.answer('Пока, админ!', reply_markup=kb)

@admin_router.message(Command(commands=['stop', 'stat', 'log']), IsAdmin(admins))
async def admin_menu(message: Message, command: CommandObject):
    if command.text == '/stop':
        logger.info('/stop')
        await dp.stop_polling()
        await bot.close()
        await exit(0)
    elif command.text == '/stat':
        logger.info('/stat')
    elif command.text == '/log':
        logger.info('/log')
    else:
        logger.info('missed command')
    msg = await message.answer('Удаляю...', reply_markup=ReplyKeyboardRemove())
    await msg.delete()
