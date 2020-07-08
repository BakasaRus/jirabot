import telebot
import socket
import os
from jira import JIRA

tokenbot = "1199790744:AAHJm58PvSbg4QaKX9dN3EAQ6Z7OcHao_Lk"
token = "kEBVkI4tySb0leegj8wuFC8F"
login = "lizafranken32@gmail.com"
api_key = "toCraz-7rimti-cemkih"

bot = telebot.TeleBot(tokenbot)

a = 0


# Connecting to Jira
#jira_options = {'server': 'https://telebotitmo.atlassian.net'}
#jira = JIRA(options=jira_options, basic_auth=(login, api_key))

@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id
    bot.send_message(user, "Если вы хотите подписться на уведомления - отправьте '/agree'")


#@bot.message_handler(content_types=['text'])
#def start(message):
#    if message.text == "/start":
#        bot.send_message("Если вы хотите подписться на уведомления - отправьте '/agree'")


@bot.message_handler(content_types=['text'])
def find(message):
#@bot.message_handler(commands=['agree'])
#def start(message):
    if message.text == "/agree":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        user = message.chat.id
        bot.send_message(user, 'Подписка на уведомления оформлена')
        while True:
            # Opening port
            s = socket.socket()  # Create a socket object
            host = socket.gethostname()  # Get local machine name
            port = 6942  # Reserve a port for your service.
            s.bind((host, port))  # Bind to the port
            s.listen(3)  # Now wait for client connection.

            workSocket, address = s.accept()     # Establish connection with client.
            bot.send_message(user, 'Got connection from', address)

            fileJSON = open("changes.json", 'wb')  # Open in binary
            while True:

                # Fill fileJSON by portions
                portionOfInformation = workSocket.recv(1024)
                while portionOfInformation:
                    fileJSON.write(portionOfInformation)
                    portionOfInformation = workSocket.recv(1024)
            fileJSON.close()

            # Rewrite json to dictionary
            with open('changes.json', 'r', encoding='utf-8') as newFileJSON:
                dictData = json.load(newFileJSON)
                bot.send_message(user, 'succeeded')

            x = dictData["toString"]
            bot.send_message(user, x)

            # fileJSON = open("changes.json", 'wb')
            # fileJSON.remove()

            # os.remove("changes.json")

bot.polling(none_stop=True)






