import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

# ========== متغيرات البيئة ==========
API_TOKEN = os.getenv("BOT_TOKEN")

# ========== إعدادات Aiogram ==========
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# ========== هاندلر /start ==========
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="🎁 افتح الميني أب",
        web_app=types.WebAppInfo(url="https://telegramconnect.onrender.com/")
    )
    keyboard.add(btn)
    await message.reply("أهلاً بك! اضغط الزر أدناه:", reply_markup=keyboard)

# ========== FastAPI وهمية فقط لريندر ==========
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Polling bot is running!"}

# ========== تشغيل البوت ==========
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)