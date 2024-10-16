from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

start_router = Router() 


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello, world")