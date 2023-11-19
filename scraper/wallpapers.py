#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
from telebot.types import InputMediaPhoto
import requests

base_url = "https://wallpapers.com"
search_url = "https://wallpapers.com/search/"

def get_wallpapers(query: str, page: int = 1):
    searchUrl = search_url + query
    response = requests.get(searchUrl)
    number = 10
    if response.status_code == 200:
        try:
            soup = bs(response.content, 'html.parser')
            files = soup.select("img.promote")
            for img in files[page * 10 :(page+1) * 10]:
                yield InputMediaPhoto(base_url+(img['data-src']).replace("hd", "file"))
        except Exception as e:
            print(f"Error: {e}")
    else:
        return False

# print(len([i for i in get_wallpapers("thor")]))