import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def handle_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text="🎁 افتح الميني أب",
            web_app=types.WebAppInfo(
                url="https://worker-1-fxao.onrender.com/"  # <-- رابط الميني أب الجديد
            )
        )
    )
    await message.answer("أهلاً بك! اضغط الزر لتفتح الميني أب 🎉", reply_markup=keyboard)

if __name__ == "__main__":
    print("🚀 Bot is running...")
    executor.start_polling(dp, skip_updates=True)