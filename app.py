#!/usr/bin/env python

import telebot
import os
from scraper.dadjokes import get_dad_jokes
from scraper.wallpapers import get_wallpapers
from telebot.types import InputMediaPhoto

global bot
global TOKEN

TOKEN = "6755079674:AAEx--Z2ijHYd9ASfXikXAdp9pSOmpbkhP4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "hello"])
def send_message(message):
    bot.reply_to(message, "Sup")

@bot.message_handler(commands=["dadjokes"])
def dad_jokes(message):
    bot.send_message(message.chat.id, get_dad_jokes(), parse_mode="Markdown")

@bot.message_handler(commands=["wallpaper"])
def get_query(message):
    text = "What wallpapers are you looking for?"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_wallpapers)

def fetch_wallpapers(message):
    name = message.text
    bot.send_media_group(chat_id=message.chat.id, media=[InputMediaPhoto(i) for i in get_wallpapers(name)])

bot.infinity_polling()