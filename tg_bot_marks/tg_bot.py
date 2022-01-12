import parse
from telebot import types
import telebot
token = "5061060127:AAE6A1Gi7JAXHnGVynrjHMH6eP1n1F64Stc"
data = []
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("Ира")
	item2=types.KeyboardButton("Лена")
	markup.add(item1,item2)
	bot.send_message(message.chat.id,'Выбирай', reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_welcome(message):
		bot.send_message(message.chat.id,'Да поможет тебе бог')

@bot.message_handler(content_types=['text'])
def nubers(message):
    if(message.text=='Ира'):
        bot.send_message(message.chat.id,'Подождите чуть-чуть')
        ans = ''
        data = parse.parse(1)
        for i in range(0,len(data),2):
            ans+=data[i]+' : '+data[i+1]+'\n'
        bot.send_message(message.chat.id,ans)
        
    elif(message.text =='Лена'):
        bot.send_message(message.chat.id,'Подождите чуть-чуть')
        ans = ''
        data = parse.parse(0)
        for i in range(0,len(data),2):
            ans+=data[i]+' : '+data[i+1]+'\n'
        bot.send_message(message.chat.id,ans)
    else:
        bot.send_message(message.chat.id,'Не понял что вы хотели')
bot.infinity_polling()