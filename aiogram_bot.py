from os.path import normpath, join
from os import listdir
from random import choice #??????????????????????
import logging
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardMarkup, InlineQuery
# import sqlalchemy

base = declarative_base

# class MediaIds(base):
#     __tablename__ = 'Media ids'
#     id = Column(Integer, primary_key=True)
#     file_id = Column(String(255))
#     filename = Column(String(255))

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

btn_hi = KeyboardButton('Я кнопка bth_hi')
btn_end = KeyboardButton('Я кнопка btn_end')
btn_atr = ReplyKeyboardMarkup()
btn_atr.add(btn_hi).add(btn_end)
InlineQuery('/start')


@dp.message_handler(commands=['start'], commands_prefix='#')
async def send_welcome_start(message: types.Message):
    """
    This handler will be called when user sends `#start` or `/help` command
    """
    await message.reply("Привет, этот бот скоро порвёт твоё очко.")


@dp.message_handler(commands=['help'], commands_prefix='#')
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `#start` or `/help` command
    """
    await message.reply("Скоро здесь будут интересные команды.", reply_markup=btn_atr)

@dp.message_handler(commands=['photo', 'Photo'], commands_prefix='#')
async def send_photo(message: types.Message):

    path = normpath('Pictures')
    random_image = choice(listdir(path))

    full_path = f'{join(path,random_image)}'
    print(full_path)
    file = await bot.download_file(full_path)
    # print(f'{file.cr_code}\n{file.cr_frame}\n{file.cr_running}\n{file}')
    file_url = bot.get_file_url(file_path=full_path)
    # photo_id = message.photo #TODO
    # print(await bot.get_file(photo_id))
    print(file_url)
    # print(file_url)
    # print(bot.get_file(file_url))
    # await message.answer_photo(photo=full_path, parse_mode=file_url)
    await bot.send_photo(chat_id=message.from_user.id, photo=full_path)
    #chat_id=message.from_user.id, photo=full_path, reply_to_message_id=message.message_id)
    # await bot.send_photo(chat_id=message.from_user.id, photo=full_path, reply_to_message_id=message.message_id, caption='1')
    # message.answer_media_group(media=full_path)
    # await message.answer_photo(photo=full_path)
    # await message.reply_photo(photo=full_path)
    # await bot.send_message(message.from_user.id, 'какой то текст')
    # await bot.send_photo(message.from_user.id, full_path)
    # await message.answer_photo(photo = f'{path}/{random_image}')

# @dp.message_handler(content_types=['photo'])  TODO работает
# async def handle_docs_photo(message):
#
#     await message.photo[-1].download('test.jpg')

@dp.message_handler()
async def echo(message: types.Message):

    user_name = f"user-name - {message.from_user['username']}, first_name - {message.from_user['first_name']}"
    print_message = message.text
    await message.answer(f'Ассам алеёкууум!!!!!!!!!!!!!!!, этот пользователь - "{user_name}", написал - "{print_message}"')
    print(f'{user_name} написал это сообщение "{print_message}"')

executor.start_polling(dp)