import asyncio
from create_bot import bot, dp, scheduler
from handlers.inline_menu import inline_router
from handlers.start import start_router
# from work_time.time_func import send_time_msg
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats

async def set_all_comads():
    commands = [BotCommand(command='/start', description='Запуск'),
                BotCommand(command='/who_am_i', description='Узнать о себе'),
                BotCommand(command='/menu', description='Общее меню'),
                BotCommand(command='/inline_menu', description='Мини меню')
                ]
    await bot.set_my_commands(commands)

async def set_private_comads():
    commands = [BotCommand(command='/start', description='Запуск'),
                BotCommand(command='/who_am_i', description='Узнать о себе'),
                BotCommand(command='/menu', description='Общее меню'),
                BotCommand(command='/inline_menu', description='Мини меню'),
                BotCommand(command='/user_menu', description='Приватное меню')]
    await bot.set_my_commands(commands, BotCommandScopeAllPrivateChats())

async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()
    dp.include_router(start_router)
    dp.include_router(inline_router)
    dp.startup.register(set_all_comads)
    dp.startup.register(set_private_comads)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
#    await set_all_comads()
#    await set_private_comads()

if __name__ == "__main__":
    asyncio.run(main())