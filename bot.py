import telebot
import socket
from jira import JIRA

tokenbot = "406696396:AAFDf1SIqBuRZodIXwYN1iNEUFYnfRIacvs"
token = "kEBVkI4tySb0leegj8wuFC8F"
login = "lizafranken32@gmail.com"
api_key = "toCraz-7rimti-cemkih"

bot = telebot.TeleBot(tokenbot)

a = 0


# Connecting to Jira
jira_options = {'server': 'https://telebotitmo.atlassian.net'}
jira = JIRA(options=jira_options, basic_auth=(login, api_key))


# Opening port
s = socket.socket()         # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 6942                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(3)                 # Now wait for client connection.

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/start":
        bot.send_message("Если вы хотите подписться на уведомления - отправьте '/agree'")



@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/agree":
        while True:
            workSocket, address = s.accept()     # Establish connection with client.
            print('Got connection from', address)

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
                bot.send_message('succed')

            x = dictData["toString"]
            bot.send_message(x)





