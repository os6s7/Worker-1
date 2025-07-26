import os
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

app = Flask(__name__)

@app.route("/")
def home():
    return "🤖 Bot is alive!"

@dp.message_handler(commands=["start"])
async def handle_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text="🎁 افتح الميني أب",
            web_app=types.WebAppInfo(
                url="https://worker-1-fxao.onrender.com/"
            )
        )
    )
    await message.answer("أهلاً بك! اضغط الزر لتفتح الميني أب 🎉", reply_markup=keyboard)

def run_bot():
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)