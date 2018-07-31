from flask import Blueprint, Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
from project.csv_data.data import * 
#from project.csv_data.graph2 import *
import numpy as np
import pandas as pd
import os 


mod = Blueprint('csv_data', __name__,template_folder='templates', static_folder='static',
                                                static_url_path='/static')

@mod.route('/csv_home')
def homepage():
    #Creating ojects
    data = Data()

    csv_data_file = os.path.join(mod.root_path, 'data/Video_Games_Sales.csv')
    game_data = pd.read_csv(csv_data_file)
    # school_shooting_data = os.path.join(mod.root_path, 'data/school_shootings.csv')
    # school_shooting_data = pd.read_csv(school_shooting_data)

    years, shootings, game_ratings = data.create_dataframe_games_shootings(game_data, school_shooting_data)
    create_Graph.create_shooting_rating_graph(years, game_ratings, shootings)
    
    score_sales_correlation = data.correlation_globalSales_criticScore(game_data)
    score_sales_correlation_US = data.correlation_USSales_criticScore(game_data)
    mean_game_rating = data.average_game_rating(game_data)
    return render_template('csv_data/csv_index.html', score_sales_correlation = score_sales_correlation, 
        mean_game_rating = mean_game_rating, score_sales_correlation_US = score_sales_correlation_US)


########## AJAX Functions below this line #################

#This route will deal with getting the max rating of a video game by year and genre 
@mod.route('/_by_max_rating')
def by_max_rating():
    year = request.args.get('year', 0, type=int)
    genre = request.args.get('genre', 0, type=str)
    #Creating a data object to interact with the data class which 
    #handles the data. 
    data = Data() 
    csv_data_file = os.path.join(mod.root_path, 'data/Video_Games_Sales.csv')
    game_data = pd.read_csv(csv_data_file)
    game_title = data.get_rating_based_year_genre(game_data, year, genre)
    return jsonify(result = game_title)

#This route will deal with getting the max earnings of a video game by genre 
@mod.route('/_by_max_earnings')
def by_max_earning():
    genre = request.args.get('genre', 0, type=str)
    data = Data()
    csv_data_file = os.path.join(mod.root_path, 'data/Video_Games_Sales.csv')
    game_data = pd.read_csv(csv_data_file)
    game_title_max_earnings = data.get_earnings_based_genre(game_data, genre)
    return  jsonify(result = game_title_max_earnings)


@mod.route('/_by_game_title')
def by_title():
    csv_data_file = os.path.join(mod.root_path, 'data/Video_Games_Sales.csv')
    game_data = pd.read_csv(csv_data_file)
    gameTitle = request.args.get('genre', 0, type=str)
    data = Data()
    critic_score = data.get_critic_score_of_game(game_data, gameTitle)
    return  jsonify(result = critic_score)
