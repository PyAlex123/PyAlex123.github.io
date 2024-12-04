import telebot
from telebot import types
from telebot.types import WebAppInfo


# Configuration
API_TOKEN = '1749907475:AAHwE4OCy0-UeGyrS9qWr4yGjO6sjWOmt5k'
bot = telebot.TeleBot(API_TOKEN)

welcome_text ="""Привет, это Данте Редгрейв👋 Чтобы начать продвижение своих видео в Интернете, заполните короткий бриф (кнопка ниже) 👇
После заполнения я напишу вам сюда. Мы назначим бесплатный онлайн-созвон, чтобы найти верный способ продвинуть ваш контент 📈"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.chat.id)
    kb = types.InlineKeyboardMarkup(row_width=1)
    breaf_btn = types.InlineKeyboardButton(text='Заполнить Бриф', web_app=WebAppInfo(url="http://127.0.0.1:5500/"))
    kb.add(breaf_btn)
    bot.send_message(message.chat.id, welcome_text,reply_markup=kb)


bot.polling()