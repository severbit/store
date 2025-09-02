from dotenv import load_dotenv
import os

# Загружаем .env файл
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
