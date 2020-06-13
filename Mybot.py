import telebot
import mysql.connector
import Mytoken


from datetime import datetime
TOKEN=Mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
from telebot import apihelper
waktusekarang=datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start', 'help'])
    def start(message):
        photo = open('img/bot.png', 'rb')
        myBot.send_photo(message.from_user.id, photo)
        teks = Mytoken.SAPA + "\n-- admin & developer @juliusryan - SMK Taruna Bhakti -- "+"\n" \
                              "hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)



print("-- Bot is active --")
myBot.polling(none_stop=True)