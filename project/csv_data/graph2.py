#This file will make the graph on matplotlib 
#importing all libraries 
import matplotlib.pyplot as plt
import numpy as np

class create_matPlotLib_Graph():

    def __init__(self):
        self.game_data = pd.read_csv('data/Video_Games_Sales.csv')
        self.game_data = pd.read_csv('data/school_shootings.csv')

    def create_shooting_rating_graph(self, years, game_ratings, shootings):
        plt.plot(game_ratings, years)
        # plt.plot(x, 3 * x)
        # plt.plot(x, 4 * x)

        # plt.legend(['y = x', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')

        plt.show()


# test = create_matPlotLib_Graph()
# test.create_shooting_rating_graph()