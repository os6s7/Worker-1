import os
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.webhook import get_new_configured_app
from aiogram.utils.executor import start_webhook
import logging

API_TOKEN = os.getenv("BOT_TOKEN", "8229929028:AAHv5EuXqcGN-BHEjCrCt6VmklQY5LibLsc")
WEBHOOK_HOST = "https://worker-1-fxao.onrender.com"
WEBHOOK_PATH = ""
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

app = FastAPI()

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

@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()

@app.post("/")
async def telegram_webhook(req: Request):
    update = types.Update(**await req.json())
    await dp.process_update(update)
    return {"ok": True}

@app.get("/")
async def root():
    return {"status": "Bot is alive!"}