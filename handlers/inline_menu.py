from aiogram.types import CallbackQuery
from aiogram import F, Router


inline_router = Router()

@inline_router.callback_query(F.data.in_(['LMK', 'RMK']))
async def process_buttons_press(callback: CallbackQuery):
    #await callback.answer()
    await callback.message.edit_text(
        text='Ты - ' + callback.from_user.full_name + ' жмакнул: ' + callback.data
             + ' в чатике: "' + callback.message.chat.full_name + '" у сообщения №' + str(callback.message.message_id),
        reply_markup=callback.message.reply_markup
    )