from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.database.queries import push_users_from_txt

start_router = Router() 


@start_router.message(F.document)
async def cmd_start(message: Message, bot: Bot):
    
    file_path = await bot.get_file(message.document.file_id)
    file = await bot.download_file(file_path, 'test.txt')

    users = open('test.txt', 'r').read().split('\n')
    print(users)
    await push_users_from_txt(file)