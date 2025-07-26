import os
import asyncio
import threading
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Mini App button
@dp.message_handler(commands=["start"])
async def handle_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        text="🎁 افتح الميني أب",
        web_app=types.WebAppInfo(url="https://worker-1-fxao.onrender.com/")
    ))
    await message.answer("أهلاً بك! جرّب الميني أب من الزر:", reply_markup=keyboard)

# Create FastAPI app
app = FastAPI()

# Run bot in a separate thread to not block FastAPI
def start_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(dp.start_polling())

@app.on_event("startup")
async def on_startup():
    threading.Thread(target=start_bot).start()

@app.get("/")
async def root():
    return {"message": "Bot is running"}