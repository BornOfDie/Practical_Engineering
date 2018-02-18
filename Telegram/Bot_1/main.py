import telebot
import constant

bot = telebot.TeleBot(constant.token)

@bot.message_handler(commands=['start', 'help'])
def handle_help_start(message):
    bot.send_message(message.chat.id, constant.help_answer)
    bot.send_message(message.chat.id, 'Будет это!')
    bot.send_message(message.chat.id, constant.help_answer + constant.addition, parse_mode='html')
    log(message)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, message.text, parse_mode='html')
    log(message)

def log(message):
    print("\n ------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \nТекст = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id), message.text))

bot.polling(none_stop=True)