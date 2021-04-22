import logging
import aiogram.kb as kb
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardMarkup


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

btn_hi = KeyboardButton('Я кнопка bth_hi')
btn_atr = ReplyKeyboardMarkup()
btn_atr.add(btn_atr)


@dp.message_handler(commands=['start'])
async def send_welcome_start(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет, этот бот скоро порвёт твоё очко.", reply_markup=kb.btn_atr)


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Скоро здесь будут интересные команды.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer('Ассам алеёкууум!!!!!!!!!!!!!!!')

executor.start_polling(dp, skip_updates=True)