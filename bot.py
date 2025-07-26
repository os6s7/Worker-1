from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os
import asyncio

app = FastAPI()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def handle_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        text="🎁 افتح الميني أب",
        web_app=types.WebAppInfo(url="https://worker-1-fxao.onrender.com/")
    ))
    await message.answer("أهلاً بك! جرّب الميني أب من الزر:", reply_markup=keyboard)

async def run_bot():
    await executor.start_polling(dp, skip_updates=True)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run_bot())

@app.get("/")
async def root():
    return {"status": "Bot is running!"}