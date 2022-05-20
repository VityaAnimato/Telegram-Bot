import telebot
import config 


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start", "help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Воспользуйтесь следующими командами:')
    bot.send_message(m.chat.id, '/values - валюты, доступные для конвертации')
    bot.send_message(m.chat.id, '/calc - конвертировать валюту')


@bot.message_handler(commands=["values"])
def values(m, res=False):
    bot.send_message(m.chat.id, 'Dollar, Euro, Ruble')
    bot.send_message(m.chat.id, '/calc - конвертировать валюту')


@bot.message_handler(commands=["calc"])
def calc(m, res=False):
    bot.send_message(m.chat.id, 'pass')
    bot.send_message(m.chat.id, 'pass')


    
# Запускаем бота
bot.polling(none_stop=True, interval=0)
