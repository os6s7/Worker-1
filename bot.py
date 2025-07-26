import os
import asyncio
import threading
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

app = FastAPI()

@dp.message(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text="🎁 افتح الميني أب",
            web_app=types.WebAppInfo(url="https://telegram-web-app-j6du.onrender.com/")
        )
    )
    await message.answer("أهلاً بك! جرّب الميني أب من الزر:", reply_markup=keyboard)

def run_bot():
    asyncio.run(dp.start_polling())

@app.on_event("startup")
async def on_startup():
    threading.Thread(target=run_bot, daemon=True).start()

@app.get("/")
async def root():
    return {"message": "Bot is running"}