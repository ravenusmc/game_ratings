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

    #This method will generate the graph with the states color coded by who won them-Clinton or Trump
    def generate_graph_rating_world_sales(self):
        #Creating an output file 
        output_file("bokeh_graph.html")

        self.data = self.data[self.data.Year_of_Release == 2006]
        
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

    #This method created the CSV file of the number of games by year. 
    def generate_csv_graph_game_count_by_year(self):
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

    #This method will create the graph from the game.csv file. 
    def create_graph_game_count_by_year(self):
        #Creating an output file 
        output_file("game_count.html")

        file = 'GC.csv'

        game_data = pd.read_csv(file)

        video_game_data = ColumnDataSource(game_data)

        plot = figure(x_axis_label='Year', y_axis_label='Game Count',
        plot_width=600, plot_height=500, tools='pan,wheel_zoom,box_zoom,reset,hover,save', 
        title='Number of Games By Year')

        plot.vbar(x='year', width=0.5, bottom=0,
        top='count', source=video_game_data, color="firebrick")

        hover = plot.select_one(HoverTool)
        hover.tooltips = [('Year', '@year'),
        ('Number of Games', '@count')]
        
        show(plot)

    #This method will create the CSV files for each game system 
    def create_csv_graph_game_count_by_system(self):
        # game_systems = ['Wii', 'NES', '2600', '3DO', '3DS', 'DS', 'GB','X360', 'PS3', 'PS2', 'SNES', 'PS4', 'N64',
        # 'WiiU', 'XOne', 'PS', 'XB']
        game_systems = ['GC']
        for game_system in game_systems:
            game_count_by_year = {}
            year = 1980 
            csv_file_title = game_system + '.csv'
            with open(csv_file_title, "w") as csv_file:
                csv_writer = writer(csv_file)
                csv_writer.writerow(["year", "count"])
                while year < 2017:
                    year_data_set = self.data[(self.data.Year_of_Release == year) & (self.data.Platform == game_system)]
                    count = year_data_set['Name'].count()
                    game_count_by_year[year] = count
                    csv_writer.writerow([year, count])
                    year += 1




graph = Graph()
# graph.generate_graph_rating_world_sales()
# graph.create_graph_game_count_by_year()
#graph.create_csv_graph_game_count_by_system()
graph.create_graph_game_count_by_year()
