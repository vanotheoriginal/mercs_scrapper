import telebot
from main import __update

token = '1792970220:AAHlSAUs8YUugE_xdUrhjzFIE9ZIX8scVYA'

app = telebot.TeleBot(token)

commands = ['/start - start the bot', '/maps - get info about maps', '/rotation - get the map rotation']


@app.message_handler(commands=['start'])
def user_start(message):
    __help = ''.join('\n').join(commands)
    app.send_message(message.chat.id, __help)


@app.message_handler(commands=['maps'])
def user_start(message):
    app.send_message(message.chat.id, __update(1))


@app.message_handler(commands=['rotation'])
def user_start(message):
    app.send_message(message.chat.id, __update(0))


app.polling()