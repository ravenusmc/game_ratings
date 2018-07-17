#This file will contain all of the code for the scraping of the metacritic website 
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

class Web_Scraping():

    def get_data_based_on_game_title(self, gameTitle, gameSystem):
        url = "http://www.metacritic.com/game/" + gameSystem + '/' + gameTitle + '/critic-reviews'
        #url="http://www.metacritic.com/game/playstation-4/god-of-war"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        soup = BeautifulSoup(web_byte, "html.parser")
        #print(bs)
        get_divs = soup.find_all(class_='review_grade')
        review_grades = []
        for div in get_divs:
            review_grade = div.get_text()
            review_grade = review_grade.strip('\n')
            if review_grade != '':
                review_grade = float(review_grade)
                review_grades.append(review_grade)
        return review_grades

# scrape = Web_Scraping()
# scrape.get_data_based_on_game_title('god-of-war',  'playstation-4')

