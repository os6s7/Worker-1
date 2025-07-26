import os
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

app = FastAPI()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# تأكد من أن البوت متصل
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="🎁 افتح الميني أب",
        web_app=types.WebAppInfo(url="https://telegram-web-app-j6du.onrender.com/"
    )
    keyboard.add(btn)
    await message.reply("أهلاً بك! اضغط الزر أدناه:", reply_markup=keyboard)

async def start_bot():
    await dp.start_polling()

@app.on_event("startup")
async def startup():
    asyncio.create_task(start_bot())

@app.get("/")
async def root():
    return {"status": "Bot is alive!"}
