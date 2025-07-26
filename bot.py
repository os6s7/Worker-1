import os
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

app = Flask(__name__)

@dp.message_handler(commands=["start"])
async def handle_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        text="🎁 افتح الميني أب",
        web_app=types.WebAppInfo(
            url="https://telegram-web-app-j6du.onrender.com/"
        )
    ))
    await message.answer("أهلاً بك! جرّب الميني أب من الزر:", reply_markup=keyboard)

@app.route("/")
def index():
    return "Bot is running fine."

async def on_startup(dp):
    print("🚀 Bot started!")

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(dp.start_polling())
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

if __name__ == "__main__":
    main()
