from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
 
kb = [
    [KeyboardButton(text="Найти")],
    [KeyboardButton(text="Добавить"), KeyboardButton(text="Схема")],
] 

kb = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True
)


search_options_kb = [
    [KeyboardButton(text="По названию 🪧"), KeyboardButton(text="По артикулу 📃")],
    [KeyboardButton(text="По местоположению 🗺")],
    [KeyboardButton(text="Отмена 🔴")]
]

search_options_kb = ReplyKeyboardMarkup(
    keyboard=search_options_kb,
    resize_keyboard=True
)