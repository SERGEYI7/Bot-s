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

list_path_pictures = os.listdir('Pictures')
count = int()


def start(update: Update, context: CallbackContext):
    # global count
    # count += 1
    # update.message.reply_text(fr'{count} -- ')
    update.message.reply_text(r'Здесь будет бот который шлёт картинки или другие медиа')


def help(update: Update, context: CallbackContext):
    update.message.reply_text(r'Вызвана команда help!!!')


# def button(update: Update, contexe: CallbackContext):
#     update.message.reply_text(r'Ваш выбор', reply_markup=markup)


def varan(update: Update, context: CallbackContext):
    rand_list_path_pictures = choice(list_path_pictures)
    update.message.reply_photo(open(os.path.join('Pictures', rand_list_path_pictures), 'rb'))
    update.message.reply_text(rand_list_path_pictures)


updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(CommandHandler('help', help))

# updater.dispatcher.add_handler(CommandHandler('button', button))

updater.dispatcher.add_handler(CommandHandler('varan', varan))


updater.start_polling()
updater.idle()