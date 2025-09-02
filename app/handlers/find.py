from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message

router = Router()
@router.message(Command("find"))
async def find_product_command(message: Message):
    await message.answer("Функция поиска товара в разработке. Пожалуйста, попробуйте позже.")
