from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.getenv("BOT_TOKEN")

if not API_TOKEN:
    raise ValueError("Bot token not found in environment variables!")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Салом! Бу сизинг ботингиз.")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
