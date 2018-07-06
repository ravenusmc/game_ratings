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

    # def __init__(self):
    #     self.game_data = pd.read_csv('data/Video_Games_Sales.csv')

    def get_rating_based_year_genre(self, data):
        print(data.head())

    # def test(self):
    #     print('The test method is working')

# data = Data()
# data.get_rating_based_year_genre()



