#This file will contain all of the code for the scraping of the metacritic website 
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

class Web_Scraping():

    def get_data_based_on_game_title(self, gameTitle):
        url="http://www.metacritic.com/game/playstation-4/god-of-war"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        bs = BeautifulSoup(web_byte,"html.parser")
        print(bs)

