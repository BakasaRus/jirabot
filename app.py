from flask import Flask
from flask import request
import json
from .bot import bot


app = Flask(__name__)


@app.route('/webhook')
def webhook():
    # Вот тут надо доставать откуда-то ID для рассылки
    data = request.get_json()
    response = json.dumps(data, indent=2)
    # И слать по полученному списку
    # bot.send_message()
    return response, 200
