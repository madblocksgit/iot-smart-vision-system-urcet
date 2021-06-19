# pip install pyTelegramBotAPI
# pip install python-telegram-bot

import telebot

token='1868136782:AAFoE7leYK9VKGOcSRj6WIJnQBLimDjnt3o'
bot = telebot.TeleBot(token, parse_mode=None) 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 bot.reply_to(message, "Welcome to IoT Smart Vision Bot by URCET, what you want me to do? \n 1. /recordvideo \n 2. /stopvideo \n 3. /callpolice")

@bot.message_handler(commands=['recordvideo'])
def record_video(message):
 if (message.chat.id==976034970 or message.chat.id==1245030246):
  bot.reply_to(message,"Video Recorded Started")
  f=open('log.txt','w')
  f.write('start')
  f.close()
 else:
  bot.reply_to(message,"Sorry, you can't do that")
 
@bot.message_handler(commands=['stopvideo'])
def record_video(message):
 if (message.chat.id==976034970 or message.chat.id==1245030246):
  bot.reply_to(message,"Video Recorded Stopped")
  f=open('log.txt','w')
  f.write('stop')
  f.close()
 else:
  bot.reply_to(message,"Sorry, you can't do that")

@bot.message_handler(commands=['callpolice'])
def record_video(message):
 if (message.chat.id==976034970 or message.chat.id==1245030246):
  bot.reply_to(message, 'Intruder Occured at Lt: 16.5509302 N , Lg: 80.6463674 E')
  bot.send_photo(976034970, open('test.jpg','rb'))
  bot.send_photo(1245030246,open('test.jpg','rb'))
 else:
  bot.reply_to(message,"Sorry, you can't do that")

def listener(messages):
 for m in messages:
  print(str(m))

bot.set_update_listener(listener)
bot.polling()