import telebot


tokenbot = "1234522170:AAHCG2bvkq8YwPdck5nCO8D0Gapuq_TmUS4"
bot = telebot.TeleBot(tokenbot)


@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id
    bot.send_message(user, "Если вы хотите подписться на уведомления - отправьте '/agree'")


@bot.message_handler(commands=['agree'])
def agree(message):
    # Вот здесь надо куда-нибудь записывать ID пользователя для рассылки
    user = message.chat.id
    bot.send_message(user, 'Подписка на уведомления оформлена')


if __name__ == '__main__':
    bot.polling(none_stop=True)
