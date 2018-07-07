#This file will build all of the graphs for the csv data file 

#Importing libraries for use in this file
from bokeh.charts import Bar, Scatter, output_file, show
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource, figure, output_file, show
from bokeh.models import CategoricalColorMapper, HoverTool
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

        #loading the csv to the file 
        file = 'data/Video_Games_Sales.csv'
        #Reading and then storing the csv file as a variable. 
        data = pd.read_csv(file)
        #Turning the data into a ColumnDataSource 
        video_game_data = ColumnDataSource(data)

        #This line will be what sets up a color code between which states voted for clinton or trump.
        # color_mapper = CategoricalColorMapper(factors=['Global_Sales', 'Critic_Score'], 
        # palette=['red', 'blue']) 

        plot = figure(x_axis_label='Critic Score', y_axis_label='Global Sales',
            plot_width=600, plot_height=500, tools='pan,wheel_zoom,box_zoom,reset,hover,save', 
            title='Game Ratings versus world sales')

        plot.circle(x='Critic_Score', y='Global_Sales', source=video_game_data, 
            size=15)

        # plot.circle(x='Critic_Score', y='Global_Sales', source=video_game_data, 
        #     size=15, color=dict(field='won_state', transform=color_mapper))

        hover = plot.select_one(HoverTool)
        hover.tooltips = [('Ratings', '@Critic_Score'),
        ('Sales', '@Global_Sales'),
        ('Game Title', '@Name')]

        show(plot)


graph = Graph()
graph.generate_graph_rating_world_sales()
