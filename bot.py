import telebot
from flask import Flask
import threading

bot = telebot.TeleBot("BOT_TOKEN")

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot ishlayapti!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! Bot ishga tushdi.")

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot).start()

app.run(host="0.0.0.0", port=8080)
