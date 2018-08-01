#This file will make the graph on matplotlib 
#importing all libraries 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class create_matPlotLib_Graph():


    def __init__(self):
        self.game_data = pd.read_csv('data/Video_Games_Sales.csv')
        self.shootings_data = pd.read_csv('data/school_shootings.csv')


    def create_dataframe_games_shootings(self):
        rating_data = self.game_data[self.game_data.Rating == "M"]
        year = 1980
        years = []
        shootings = []
        game_ratings = []
        while year < 2017:
            rating_data_year = rating_data[rating_data.Year_of_Release == year]
            count_of_games = rating_data_year['Name'].count()
            shootings_by_year = self.shootings_data[self.shootings_data.year == year]
            count_of_shootings = shootings_by_year['school_name'].count()
            years.append(year)
            shootings.append(count_of_shootings)
            game_ratings.append(count_of_games)
            year += 1
        return years, shootings, game_ratings


    def create_shooting_rating_graph(self):
        years, shootings, game_ratings = self.create_dataframe_games_shootings()
        plt.plot(years, game_ratings)
        plt.plot(years, shootings)
        plt.legend(['Game Rating "M"', 'School Shootings'], loc='upper left')
        plt.ylabel("Count")
        plt.xlabel("Year")
        plt.show()


# test = create_matPlotLib_Graph()
# test.create_shooting_rating_graph()