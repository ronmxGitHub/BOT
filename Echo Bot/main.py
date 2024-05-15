import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7136244815:AAGt0oWrs2dfJHpC8fbMg9fTX1ASSjjwais'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom\nMen EchoMxBot\nAiogram yordamida yaratilganman.")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)