from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import asyncio
from config import BOT_TOKEN # Импортируем токен из config.py

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()  # Создаём диспетчер

@dp.message(Command("app"))
async def send_web_app(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть приложение", web_app=WebAppInfo(url="https://yourdomain.com"))]
        ]
    )
    await message.answer("Запускаем приложение! 🚀", reply_markup=keyboard)

async def main():
    print("Бот запущен 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


