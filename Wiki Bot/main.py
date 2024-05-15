import wikipedia
from aiogram import executor, types,Bot, Dispatcher
import logging
API_TOKEN="7148984322:AAGgw3eEnAdxg7A47vJg43Ge0BxwxgPac9k"

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang("uz")

@dp.message_handler(commands=["start", "help"])
async def hello(message: types.Message):
    await message.answer("Assalomu alaykum\nWikipediya botimizga xush kelibsiz!\nMatningizni yuboring")


@dp.message_handler()
async def hello(message: types.Message):
    try:
        matn=message.text
        await message.answer(wikipedia.summary(matn))
    except:
        await message.answer("Bunday ma'lumot topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)