#This file will build all of the graphs for the csv data file 

#Importing libraries for use in this file
from bokeh.charts import Bar, Scatter, output_file, show
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource, figure, output_file, show
from bokeh.models import CategoricalColorMapper, HoverTool
from csv import writer
import csv
import matplotlib.pyplot as plt
import numpy as np
from nvd3 import scatterChart
import pandas as pd

class Graph():

    def __init__(self):
        self.data = pd.read_csv('data/Video_Games_Sales.csv')

    # def test(self):
    #     print(self.data.head())

    #This method will generate the graph with the states color coded by who won them-Clinton or Trump
    def generate_graph_rating_world_sales(self):
        #Creating an output file 
        output_file("bokeh_graph.html")

        self.data = self.data[self.data.Year_of_Release == 2006]

        #loading the csv to the file 
        #file = 'data/Video_Games_Sales.csv'

        #Reading and then storing the csv file as a variable. 
        #data = pd.read_csv('data/Video_Games_Sales.csv')
        #Turning the data into a ColumnDataSource 
        
        video_game_data = ColumnDataSource(self.data)

        plot = figure(x_axis_label='Critic Score', y_axis_label='Global Sales',
            plot_width=600, plot_height=500, tools='pan,wheel_zoom,box_zoom,reset,hover,save', 
            title='Game Ratings versus world sales')

        plot.circle(x='Critic_Score', y='Global_Sales', source=video_game_data, 
            size=15)

        hover = plot.select_one(HoverTool)
        hover.tooltips = [('Ratings', '@Critic_Score'),
        ('Sales', '@Global_Sales'),
        ('Game Title', '@Name')]

        show(plot)

    def generate_graph_game_count_by_year(self):
        game_count_by_year = {}
        year = 1980 
        with open("game.csv", "w") as csv_file:
            csv_writer = writer(csv_file)
            csv_writer.writerow(["year", "count"])
            while year < 2017:
                year_data_set = self.data[self.data.Year_of_Release == year]
                count = year_data_set['Name'].count()
                game_count_by_year[year] = count
                csv_writer.writerow([year, count])
                year += 1
        #print(game_count_by_year)



graph = Graph()
# graph.generate_graph_rating_world_sales()
graph.generate_graph_game_count_by_year()
