#This file will contain all of the code for the scraping of the metacritic website 
from urllib.request import Request, urlopen
import urllib, sys
from bs4 import BeautifulSoup
import pandas as pd

class Web_Scraping():

    def get_data_based_on_game_title(self, gameTitle, gameSystem):
        url = "http://www.metacritic.com/game/" + gameSystem + '/' + gameTitle + '/critic-reviews'
        print(url)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try: 
            web_byte = urlopen(req).read()
            soup = BeautifulSoup(web_byte, "html.parser")
            get_parent_div = soup.find_all(class_='critic_review')
            review_grades = []
            for div in get_parent_div:
                grade = div.find(class_='review_grade')
                review_grade = grade.get_text()
                review_grade = review_grade.strip('\n')
                if review_grade != '':
                    review_grade = float(review_grade)
                    review_grades.append(review_grade)
            return review_grades
        except urllib.error.HTTPError as err:
            review_grades = 'No Data Found!'
            return review_grades

    def convert_list_to_series(self, review_grades):
        score_dataFrame = pd.Series(review_grades)
        return score_dataFrame


    def calculate_mean(self, score_dataFrame):
        score_mean = score_dataFrame.mean()
        score_mean_formatted = format(score_mean, '.2f')
        return score_mean_formatted


    def calculate_median(self, score_dataFrame):
        score_median = score_dataFrame.median()
        score_median_formatted = format(score_median, '.2f')
        return score_median_formatted


    def calculate_standard_deviation(self, score_dataFrame):
        score_std = score_dataFrame.std()
        score_std_formatted = format(score_std, '.2f')
        return score_std_formatted
            






























