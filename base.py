import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text', 'start', 'help'])
def text_message(message):
    bot.send_message(message.from_user.id, 'Hello World!')

bot.polling()#(none_stop=True, interval=0)