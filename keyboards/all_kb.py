from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType, InlineKeyboardMarkup, \
    InlineKeyboardButton
from create_bot import admins

def main_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text="Кнопка 1"), KeyboardButton(text="И ещё кнопка")],
        [KeyboardButton(text="📝 Заполнить анкету"), KeyboardButton(text="📚 Каталог")]
    ]
    if user_telegram_id in admins:
        kb_list.append([KeyboardButton(text="⚙️ Админ панель")])
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )
    return keyboard

def private_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text="Дать контакт", request_contact=True), KeyboardButton(text="Создать опрос", request_poll=KeyboardButtonPollType())],
        [KeyboardButton(text="📝 Заполнить анкету"), KeyboardButton(text="📚 Каталог")]
    ]
    if user_telegram_id in admins:
        kb_list.append([KeyboardButton(text="⚙️ Админ панель")])
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )
    return keyboard


def mini_kb(user_telegram_id: int):
     kb_list = [
         [InlineKeyboardButton(text="LMK", callback_data='LMK'), InlineKeyboardButton(text="RMK", callback_data='RMK')]
     ]
     keyboard = InlineKeyboardMarkup (
         inline_keyboard=kb_list
     )
     return keyboard