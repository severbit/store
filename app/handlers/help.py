from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message
from app.messages import help_message
router = Router()

@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(text=help_message)
