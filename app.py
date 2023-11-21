#!/usr/bin/env python

import telebot
import os
from time import sleep
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

@bot.message_handler(commands=["wallpaper", "wallpapers"])
def get_query(message):
    msg = (message.text).split()
    msg = " ".join(msg[1:])
    text = f"Looking for {msg.upper()}"
    bot.send_message(message.chat.id, text, parse_mode="Markdown")
    sent_walls = bot.send_media_group(chat_id=message.chat.id, media=[i for i in get_wallpapers(msg)])
    bot.register_next_step_handler(sent_walls[-1], fetch_more_pics, msg)

def fetch_more_pics(message, msg):
    message = message.text
    if "more" in message:
        text = f"Looking for more {msg} wallpaper"
        bot.send_message(message.chat.id, text, parse_mode="Markdown")
        sent_walls = bot.send_media_group(chat_id=message.chat.id, media=[i for i in get_wallpapers(msg, 2)])

@bot.edited_message_handler(commands=["wallpaper", "wallpapers"])
def get_edited_query(message):
    msg = (message.text).split()
    msg = " ".join(msg[1:])
    text = f"Looking for {msg.upper()}"
    bot.send_message(message.chat.id, text, parse_mode="Markdown")
    sent_walls = bot.send_media_group(chat_id=message.chat.id, media=[i for i in get_wallpapers(msg, 2)])

@bot.message_handler(commands=["test"])
def test_handler(message):
    test_text = "Testing..."
    bot.send_message(message.chat.id, message.text, parse_mode="Markdown")

if __name__ == "__main__":
    print("Starting Telegram Bot Server...")
    sleep(1)
    bot.infinity_polling()