from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from app.messages import search_reply_message
from app.keyboard.main import search_options_kb, kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class Find(StatesGroup):
    waiting_for_option = State()


router = Router()

@router.message(F.text == "Найти")
@router.message(Command("find"))
async def find_product_command(message: Message, state: FSMContext):
    await message.answer(text=search_reply_message,
                         reply_markup=search_options_kb)
    await state.set_state(Find.waiting_for_option)

# --- реакции на варианты ---
@router.message(Find.waiting_for_option, F.text == "По названию 🪧")
async def search_by_name(message: Message, state: FSMContext):
    await message.answer("🔍 Введите название товара:", reply_markup=ReplyKeyboardRemove())
    await state.clear()   # очищаем состояние (дальше обычный ввод)

@router.message(Find.waiting_for_option, F.text == "По артикулу 📃")
async def search_by_article(message: Message, state: FSMContext):
    await message.answer("🔍 Введите артикул товара:", reply_markup=ReplyKeyboardRemove())
    await state.clear()

@router.message(Find.waiting_for_option, F.text == "По местоположению 🗺")
async def search_by_location(message: Message, state: FSMContext):
    await message.answer("📍 Введите местоположение:", reply_markup=ReplyKeyboardRemove())
    await state.clear()

@router.message(Find.waiting_for_option, F.text == "Отмена 🔴")
async def cancel_search(message: Message, state: FSMContext):
    await message.answer("❌ Поиск отменён", reply_markup=kb)
    await state.clear()