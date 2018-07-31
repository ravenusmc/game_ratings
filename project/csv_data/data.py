#This file will deal with all of the data that this project will analyze from the csv file 

#Bringing in the files that I need:
# from bokeh.charts import Scatter, output_file, show
# from bokeh.plotting import figure, output_file, show
import csv
from csv import writer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

class Data():

    def get_rating_based_year_genre(self, data, year, genre):
        year = float(year)
        #Getting rid of all the NA values 
        data = data.dropna()
        # print(data.Genre.unique())
        #Sorting the DF by the genre and years that were entered in by the user
        data = data[(data.Genre == genre) & (data.Year_of_Release == year)]
        #print(data.head())
        #Now getting the max rating 
        max_rating = data.max()
        #getting the title from the series 
        game_title = max_rating[0]
        if isinstance(game_title, str):
            return game_title
        elif math.isnan(game_title):
            game_title = 'No games found for that year'
            return game_title

    def get_earnings_based_genre(self, data, genre):
        #Getting rid of all the NA values 
        data = data.dropna()
        data = data[data.Genre == genre]
        #getting the max earnings 
        max_earnings = data.max()
        #getting the title from the series 
        game_title = max_earnings[0]
        return game_title

    def correlation_globalSales_criticScore(self, data):
        #Getting rid of all the NA values 
        data = data.dropna()
        score_sales_correlation = data['Critic_Score'].corr(data['Global_Sales'])
        score_sales_correlation = format(score_sales_correlation, '.2f')
        return score_sales_correlation

    def average_game_rating(self, data):
        data = data.dropna()
        data = data['Critic_Score']
        mean = data.mean()
        mean = format(mean, '.2f')
        return mean

    def correlation_USSales_criticScore(self, data):
        data = data.dropna()
        score_sales_correlation_US = data['Critic_Score'].corr(data['NA_Sales'])
        score_sales_correlation_US = format(score_sales_correlation_US, '.2f')
        return score_sales_correlation_US

    def get_critic_score_of_game(self, gameData, gameTitle):
        gameData = gameData.dropna()
        gameData = gameData[gameData.Name == gameTitle]
        if gameData.empty:
            critic_score = 'No Score Found!'
        else: 
            critic_score = gameData.iat[0,10]
        return critic_score

    def build_game_list(self):
        data = pd.read_csv('./data/Video_Games_sales.csv')
        data = data.dropna()
        count = 0 
        games = []
        while count < len(data):
            game = data.iat[count, 0]
            games.append(game)
            count += 1

    def create_dataframe_games_shootings(self, game_data, school_shooting_data):
        rating_data = game_data[game_data.Rating == "M"]
        year = 1980
        years = []
        shootings = []
        game_ratings = []
        while year < 2017:
            rating_data_year = rating_data[rating_data.Year_of_Release == year]
            count_of_games = rating_data_year['Name'].count()
            shootings_by_year = school_shooting_data[school_shooting_data.year == year]
            count_of_shootings = shootings_by_year['school_name'].count()
            years.append(year)
            shootings.append(count_of_shootings)
            game_ratings.append(count_of_games)
            year += 1
        return years, shootings, game_ratings











