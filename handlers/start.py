from aiogram import Router, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.all_kb import main_kb, mini_kb, private_kb

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message, command: CommandObject):
    command_args: str = command.args
    if command_args:
        await message.answer(f'Привет! {command_args}')
    else:
        await message.answer('Привет!')

@start_router.message(Command('who_am_i'))
async def who_am_i(message: Message):
    text = ''
    user = message.from_user
    if user.username: text += f"YOU: @{user.username} "
    if user.last_name: text += f"YOUR NAME: {user.first_name} {user.last_name} "
    else: text += f"YOUR NAME: {user.first_name} "
    text += f"YOUR ID: {user.id}"
    await message.answer(text)

@start_router.message(Command('menu'))
async def menu(message: Message):
    await message.answer('Выбери действие:',
                         reply_markup=main_kb(message.from_user.id))

@start_router.message(Command('user_menu'))
async def user_menu(message: Message):
    await message.answer('Выбери действие:',
                         reply_markup=private_kb(message.from_user.id))

@start_router.message(Command('inline_menu'))
async def menu2(message: Message):
    await message.answer('Выбери действие:',
                         reply_markup=mini_kb(message.from_user.id))

@start_router.message(F.text)
async def remove_kb(message: Message):
    msg = await message.answer(str(None), reply_markup=ReplyKeyboardRemove())
    await msg.delete()

#@start_router.message(F.text == '/start_3')
#async def cmd_start_3(message: Message):
#   await message.answer('Запуск сообщения по команде /start_3 используя магический фильтр F.text!')