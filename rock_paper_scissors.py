from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, dispatcher
from telegram import Update, ReplyKeyboardMarkup, Bot
import config
import logging
from random import choice
import os
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

updater = Updater(token=config.TOKEN, use_context=True)

bot = Bot(token=config.TOKEN)

items = ['Камень', 'Ножницы', 'Бумага']
reply_keyboard = [items]
markup = ReplyKeyboardMarkup(reply_keyboard)

def stone(update: Update, context: CallbackContext):
    rand_item = choice(items)
    update.message.reply_text(fr'Против тебя выпало {rand_item}')
    if rand_item == 'Камень':
        update.message.reply_text(r'Ничья')
    elif rand_item == 'Ножницы':
        update.message.reply_text("Вы выйграли")
    elif rand_item == 'Бумага':
        update.message.reply_text('Вы проиграли')


def paper(update: Update, context: CallbackContext):
    rand_item = choice(items)
    update.message.reply_text(fr'Против тебя выпало {rand_item}')
    if rand_item == 'Камень':
        update.message.reply_text("Вы выйграли")
    elif rand_item == 'Ножницы':
        update.message.reply_text('Вы проиграли')
    elif rand_item == 'Бумага':
        update.message.reply_text(r'Ничья')


def scissors(update: Update, context: CallbackContext):
    rand_item = choice(items)
    update.message.reply_text(fr'Против тебя выпало {rand_item}')
    if rand_item == 'Камень':
        update.message.reply_text('Вы проиграли')
    elif rand_item == 'Ножницы':
        update.message.reply_text(r'Ничья')
    elif rand_item == 'Бумага':
        update.message.reply_text("Вы выйграли")


def start(update: Update, context: CallbackContext):
    update.message.reply_text(r'Ваш выбор', reply_markup=markup)


def help(update: Update, context: CallbackContext):
    update.message.reply_text(r'Вызвана команда help!!!')


updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(CommandHandler('help', help))

updater.dispatcher.add_handler(MessageHandler(Filters.regex('Бумага'), paper))

updater.dispatcher.add_handler(MessageHandler(Filters.regex('Ножницы'), scissors))

updater.dispatcher.add_handler(MessageHandler(Filters.regex('Камень'), stone))


updater.start_polling()
updater.idle()
