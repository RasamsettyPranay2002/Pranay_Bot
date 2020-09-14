import os
!pip install adafruit-io
x = "Pranay13579"
y = "aio_rAfG735cSWI71yqSnhq9fUIoOaWM"

from Adafruit_IO import Client, Feed
from Adafruit_IO import Data
aio = Client(x,y)
!pip install python-telegram-bot
from telegram.ext import Updater,CommandHandler
import requests
def turn_on_light(bot,update):
  value = Data(value=1)
  value_send = aio.create_data('bot',value)
  chat_id = update.message.chat_id
  bot.send_message(chat_id,text='The light is turned on')
  bot.send_photo(chat_id,photo='https://purepng.com/public/uploads/large/purepng.com-lamplampledswhite-lightselectric-lights-1421526579009b77xo.png')

def turn_off_light(bot,update):
  value = Data(value=0)
  value_send = aio.create_data('bot',value)
  chat_id = update.message.chat_id
  bot.send_message(chat_id,text='The light is turned off')
  bot.send_photo(chat_id,photo='https://tse3.mm.bing.net/th?id=OIP.ArFIDBnNFp2NeARkI6tIhgHaKP&pid=Api&P=0&w=300&h=300')
  u = Updater('1376734750:AAGoRkNk2_5lXTcf67f9Keibrny5giRT43Y')
dp = u.dispatcher
dp.add_handler(CommandHandler('on_light',turn_on_light))
dp.add_handler(CommandHandler('off_light',turn_off_light))
u.start_polling()
u.idle()
