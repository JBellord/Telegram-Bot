from bs4 import BeautifulSoup as bs
import requests

base_url = "https://wallpapers.com"
search_url = "https://wallpapers.com/search/"

def get_wallpapers(query: str):
    searchUrl = search_url + query
    response = requests.get(searchUrl)
    if response.status_code == 200:
        try:
            soup = bs(response.content, 'html.parser')
            files = soup.select("img.promote")
            for img in files[:10]:
                yield (base_url+(img['data-src']).replace("hd", "file"))
        except Exception as e:
            print(f"Error: {e}")
    else:
        return False

get_wallpapers("sabrina")