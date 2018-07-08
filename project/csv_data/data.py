#This file will deal with all of the data that this project will analyze from the csv file 

#Bringing in the files that I need:
# from bokeh.charts import Scatter, output_file, show
# from bokeh.plotting import figure, output_file, show
import csv
from csv import writer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

        


#checking the datatype:
#print(data.dtypes)




