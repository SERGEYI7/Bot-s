import logging
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardMarkup, InlineQuery


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

btn_hi = KeyboardButton('Я кнопка bth_hi')
btn_end = KeyboardButton('Я кнопка btn_end')
btn_atr = ReplyKeyboardMarkup()
btn_atr.add(btn_hi).add(btn_end)
InlineQuery('/start')


@dp.message_handler(commands=['start'], prefixes='!!')
async def send_welcome_start(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет, этот бот скоро порвёт твоё очко.")

  
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Скоро здесь будут интересные команды.", reply_markup=btn_atr)


@dp.message_handler()
async def echo(message: types.Message):

    user_name = f"user-name - {message.from_user['username']}, first_name - {message.from_user['first_name']}"
    print_message = message.text
    await message.answer(f'Ассам алеёкууум!!!!!!!!!!!!!!!, этот пользователь - "{user_name}", написал - "{print_message}"')
    dict_message = dict(message)
    print(f'{user_name} написал это сообщение "{print_message}"')

executor.start_polling(dp, skip_updates=True)