import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

bot = Client(
  "message-bot",
  bot_token="1943952420:AAG4yAPtx_vlFSoXa7yzDhe4xcWKenTEfMA",
  api_id="3020564",
  api_hash="91c026fadfdc442f504a0bd3e5c8cd18",
  )

@bot.on_message(filters.command(['start']))
def start(Client, messages):
  send_photo("https://telegra.ph/file/9a237eaeed7580baca00d.jpg",
  reply_markup = InlineKeyboardMarkup( # button
      [
         [
            InlineKeyboardButton('Owner', url='https://t.me/XXXTENTACION_OF_TG'),
            InlineKeyboardButton('group', url='https://t.me/MGMOVIEGRAM')
         ],
         [
            InlineKeyboardButton('help', callback_data="help"),
         ]
      ]
      )
     )
     
bot.run()
