import telebot
from config import keys, TOKEN
from extensions import APIException , CryptoConverter


bot = telebot.TeleBot(TOKEN)
        
        
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Для конвертации валюты - введите запрос в следующем формате: \
                     \n\n <валюта#1> <валюта#2> <кол-во валюты#1> \
                     \n\n например: 'euro dollar 17' \
                     \n\n /values - валюты, доступные для конвертации \
                     \n\n /help - подсказка")

@bot.message_handler(commands=["help"])
def help(m, res=False):
    bot.send_message(m.chat.id, "Введите запрос в следующем формате: \
                     \n\n <валюта#1> <валюта#2> <кол-во валюты#1> через пробел\
                     \n\n например: 'euro dollar 17' \
                     \n\n например: 'dollar ruble 33' \
                     \n\n например: 'euro ruble 47' \
                     \n\n /values - валюты, доступные для конвертации")
                    


@bot.message_handler(commands=["values"])
def values(m, res=False):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(m, text)



@bot.message_handler(content_types=["text", ])
def get_price(m, res=False):
    try:
        values = m.text.split(' ')
        
        if len(values) != 3:
            raise APIException ("Неправильный формат запроса ")
            
        quote, base, amount = values
        
        total_base = CryptoConverter.get_price(quote.lower(), base.lower(), amount)
    except APIException  as e:
        bot.reply_to(m, f'Ошибка пользователя\n{e}')
        bot.reply_to(m, f'\n/help - подсказка\n')
    except Exception as e:
        bot.reply_to(m, f'Не удалось обработать команду\n{e}')
    else:
        text = f'{amount} {quote} = {total_base} {base}'
        bot.send_message(m.chat.id, text)

    
bot.polling(none_stop=True, interval=0)
