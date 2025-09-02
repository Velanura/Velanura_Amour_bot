from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.getenv("BOT_TOKEN")  # Token from environment variable

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("👋 Ассалому алайкум!\nVelanura Amour ботга хуш келибсиз.\n\nКаталогни кўриш учун /catalog ёзинг.")

@dp.message_handler(commands=['catalog'])
async def show_catalog(message: types.Message):
    await message.answer("👗 Каталог ҳозирча тайёрланмоқда.\nЯнги коллекция тез орада!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
