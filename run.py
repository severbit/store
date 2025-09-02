from app.config import BOT_TOKEN
from aiogram import Bot, Dispatcher, types
from app.handlers import start, help
import asyncio


async def main():
    try:
        token = f'{BOT_TOKEN}'
        bot = Bot(token)
        dp = Dispatcher()
        dp.include_router(start.router)
        dp.include_router(help.router)

        print("Бот запущен")
        await dp.start_polling(bot)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        print("Бот остановлен")

if __name__ == "__main__":
    asyncio.run(main())