from googletrans import Translator
from aiogram import executor, types, Bot, Dispatcher
import logging
API_TOKEN="7090292964:AAGMMOfRFyfV2PczSKd_gTPEEsiLVhPlONM"

logging.basicConfig(level=logging.INFO)


#Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
translator=Translator()

@dp.message_handler(commands=["start", "help"])
async def hello(message: types.Message):
    await message.answer("Assalomu alaykum botimizga hush kelibsiz\nMatningizni yuboring")



@dp.message_handler()
async def get_date(message: types.Message):
    translation = translator.translate(message.text, dest='en')
    translated_text = translation.text
    await message.reply(translated_text)

if __name__ =='__main__':
    executor.start_polling(dp, skip_updates=True)