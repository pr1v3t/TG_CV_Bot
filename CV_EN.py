# CV  TelegramBot by pr1v3t
# English

import telebot
from telebot import types

API_TOKEN = 'your:token'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def corebuttons(message):
    core = types.ReplyKeyboardMarkup(True, False)
    core.row('Main information')
    core.row('Skills')
    core.row('Relevant work experience')
    core.row('Work experience')
    core.row('Contacs', 'About')  # Two buttons in a row
    # core.row('О боте') #If standalone button needed
    bot.send_message(message.chat.id, '⬇️Select a section below⬇️'.format(name=message.chat.first_name),
                     reply_markup=core)


@bot.message_handler(content_types=['text'])
def core2(message):
    if message.text == 'Main information':
        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('Main menu')
        bot.send_message(message.chat.id, 'Info about you', reply_markup=key)
    elif message.text == 'Skills':
        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('Main menu')
        bot.send_message(message.chat.id, 'Your skills', reply_markup=key)
    elif message.text == 'Relevant work experience':
        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('Main menu')
        bot.send_message(message.chat.id, 'Your relevant work experience for offer', reply_markup=key)
    elif message.text == 'Work experience':
        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('Main menu')
        bot.send_message(message.chat.id, 'Your full work experience', reply_markup=key)
    elif message.text == 'Contacs':
        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('Main menu')
        bot.send_message(message.chat.id, ' ☎️+phone \n\n📱tg nickname \n\n📧 email\n\n📷 insta',
                         reply_markup=key)
    elif message.text == 'About':
        key = telebot.types.ReplyKeyboardMarkup(True, False)
        key.row('Main menu')
        bot.send_message(message.chat.id,
                         'Version 1.0\nThis bot created by @Pr1v3t\nAlso, this bot can work in language whatever you want!',
                         reply_markup=key)
    elif message.text == 'Main menu':
        corebuttons(message)


bot.polling()
