import asyncio

from aiogram import Bot, Dispatcher

from app.handlers.registration.reg_handlers import start_router
from app.database.session import create_session
from config import TOKEN





async def main():
    await create_session()
    bot = Bot(token=TOKEN) 
    dp = Dispatcher()

    dp.include_routers(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass