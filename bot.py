from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

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

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await executor.start_polling(dp, skip_updates=True)

@app.get("/")
async def root():
    return {"message": "Bot is running!"}