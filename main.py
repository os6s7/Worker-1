import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="🎁 افتح الميني أب",
        web_app=types.WebAppInfo(url="https://telegram-web-app-j6du.onrender.com/")
    )
    keyboard.add(btn)
    await message.reply("أهلاً بك! اضغط الزر أدناه:", reply_markup=keyboard)

if __name__ == "__main__":
    # تأكد تحذف أو تلغي أي ويب هووك مفعل للبوت قبل التشغيل
    executor.start_polling(dp, skip_updates=True)