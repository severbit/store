from aiogram.filters import CommandStart
from aiogram import Router, types
from app.keyboard.main import kb
from app.messages import start_message

router = Router()

@router.message(CommandStart())
async def process_start_command(message: types.Message):
    await message.answer(text=start_message, 
                         reply_markup=kb)
