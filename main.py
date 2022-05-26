import telebot
import config
import json
import requests

bot = telebot.TeleBot(config.TOKEN)


keys = {
    'dollar': 'USD',
    'euro': 'EUR',
    'ruble': 'RUB',
}



@bot.message_handler(commands=["start", "help"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Для конвертации валюты - введите запрос в следующем формате: \
                     \n\n <валюта#1> <валюта#2> <кол-во валюты#1> \
                     \n\n например: 'euro dollar 17' \
                     \n\n /values - валюты, доступные для конвертации")
                    





@bot.message_handler(commands=["values"])
def values(m, res=False):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(m, text)


@bot.message_handler(content_types=["text", ])
def convert(m, res=False):
    quote, base, amount = m.text.split(' ')
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(m.chat.id, text)


@bot.message_handler(commands=["calc"])
def calc(m, res=False):
    # принять данные от пользователя
    bot.send_message(m.chat.id, 'get_prices(base, quote, amount)')
    # предложить посчитать еще раз


    
# Запускаем бота
    
bot.polling(none_stop=True, interval=0)
