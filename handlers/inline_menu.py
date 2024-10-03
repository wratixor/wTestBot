from aiogram.types import CallbackQuery
from aiogram import F, Router


inline_router = Router()

@inline_router.callback_query(F.data.in_(['LMK', 'RMK']))
async def process_buttons_press(callback: CallbackQuery):
    #await callback.answer()
    await callback.message.edit_text(
        text=f'Ты - {callback.from_user.full_name}'
             f' жмакнул: {callback.data} в чатике: '
             f'"{callback.message.chat.full_name}"'
             f' у сообщения №{callback.message.message_id} '
             f'uid={callback.from_user.id} '
             f'grid={callback.message.chat.id} '
             f'type={callback.message.chat.type}',
        reply_markup=callback.message.reply_markup
    )