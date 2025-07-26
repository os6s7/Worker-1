import os
import threading
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

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

def run_bot():
    executor.start_polling(dp, skip_updates=True)

app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is running fine."

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
