import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # if message == '/start':
    #     bot.reply_to(message, 'Нормально?')
    # elif message == '/help':
    bot.reply_to(message, 'есть толко команда /help и /start')

@bot.message_handler(content_types=['text'])
def text_message(message):
    bot.send_message(message.from_user.id, 'Hello World!')

# markup = types.ReplyKeyboardMarkup()
# itembtn1 = types.KeyboardButton('говна')
# markup.add(itembtn1)
# bot.send_message(chat_id=False, 'На, папей', reply_markup=markup)

bot.polling()#(none_stop=True, interval=0)

# markup = types.ReplyKeyboardMarkup(row_width=2)
# itembtn1 = types.KeyboardButton('a')
# itembtn2 = types.KeyboardButton('v')
# itembtn3 = types.KeyboardButton('d')
# markup.add(itembtn1, itembtn2, itembtn3)
# tb.send_message(chat_id, "Choose one letter:", reply_markup=markup)

# # or add KeyboardButton one row at a time:
# markup = types.ReplyKeyboardMarkup()
# itembtna = types.KeyboardButton('a')
# itembtnv = types.KeyboardButton('v')
# itembtnc = types.KeyboardButton('c')
# itembtnd = types.KeyboardButton('d')
# itembtne = types.KeyboardButton('e')
# markup.row(itembtna, itembtnv)
# markup.row(itembtnc, itembtnd, itembtne)
# bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)