from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from app.messages import search_reply_message
from app.keyboard.main import search_options_kb, kb, search_again_kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.services.find import find
import math 

class Find(StatesGroup):
    waiting_for_option = State()
    waiting_for_input = State()
    waiting_for_article = State()
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
    await state.set_state(Find.waiting_for_input) 

@router.message(Find.waiting_for_option, F.text == "По артикулу 📃")
async def search_by_article(message: Message, state: FSMContext):
    await message.answer("🔍 Введите артикул товара:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Find.waiting_for_article)


@router.message(Find.waiting_for_option, F.text == "Отмена 🔴")
async def cancel_search(message: Message, state: FSMContext):
    await message.answer("❌ Поиск отменён", reply_markup=kb)
    await state.clear()

@router.message(Find.waiting_for_input, F.text)
async def result(message: Message, state: FSMContext):
    search_query = message.text.strip()
    results = find(search_query, "name")
    print("Поиск начался")
    if not results:
        await message.answer("❌ Ничего не найдено", reply_markup=search_again_kb)
        await state.clear()
        return
    
    # Разбиваем результат на части по 4000 символов
    response = "🔍 Найдено:\n\n"
    
    for i, product in enumerate(results, 1):
        product_text = f"{i}. 📦 {product['name']}\n"
        product_text += f"   Код: {product.get('pin_code', 'Не указана')}\n"
        product_text += f"   Цена по складу: {product.get('primary_price', 'Не указана')}\n\n"
        product_text += f"   Количество: {product.get('count', 'Не указана')}\n\n"
        response += product_text
    # Отправляем остаток
    if response:
        await message.answer(response, reply_markup=search_again_kb)
    
    await state.clear()

# Обработчик кнопки "Искать снова"
@router.message(F.text == "Искать снова")
async def search_again(message: Message, state: FSMContext):
    await message.answer("Выберите метод поиска:", reply_markup=search_options_kb)
    await state.set_state(Find.waiting_for_option)

@router.message(Find.waiting_for_article, F.text)
async def result_by_article(message: Message, state: FSMContext):
    print("Поиск по артикулу")
    search_query = message.text.strip()
    results = find(search_query, "code")
    print("Поиск начался")
    if not results:
        await message.answer("❌ Ничего не найдено", reply_markup=search_again_kb)
        await state.clear()
        return
    
    # Разбиваем результат на части по 4000 символов
    response = "🔍 Найдено:\n\n"
    
    for i, product in enumerate(results, 1):
        product_text = f"{i}. 📦 {product['name']}\n"
        product_text += f"   Код: {product.get('pin_code', 'Не указана')}\n"
        product_text += f"   Цена по складу: {product.get('primary_price', 'Не указана')}\n\n"
        product_text += f"   Количество: {product.get('count', 'Не указана')}\n\n"
        response += product_text
    # Отправляем остаток
    if response:
        await message.answer(response, reply_markup=search_again_kb)
    
    await state.clear()