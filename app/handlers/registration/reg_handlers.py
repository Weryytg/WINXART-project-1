import os

from aiogram import Router, F, Bot
from aiogram.types import Message

from app.database.queries import push_users_from_txt

start_router = Router() 


@start_router.message(F.text)
async def cmd_start(message: Message):
    pass


@start_router.message(F.document)
async def cmd_start(message: Message, bot: Bot):
    
    file_path = (await bot.get_file(message.document.file_id)).file_path
    await bot.download_file(file_path, 'test.txt')
    users = open('test.txt', 'r').read().split('\n')
    await push_users_from_txt(users)
    os.remove('test.txt')