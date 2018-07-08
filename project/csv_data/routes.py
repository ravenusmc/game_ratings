from flask import Blueprint, Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
from project.csv_data.data import * 
import numpy as np
import pandas as pd
import os 


mod = Blueprint('csv_data', __name__,template_folder='templates', static_folder='static',
                                                static_url_path='/static')

@mod.route('/csv_home')
def homepage():
    data = Data()
    csv_data_file = os.path.join(mod.root_path, 'data/Video_Games_Sales.csv')
    game_data = pd.read_csv(csv_data_file)
    score_sales_correlation = data.correlation_globalSales_criticScore(game_data)
    return render_template('csv_data/csv_index.html', score_sales_correlation = score_sales_correlation)


#AJAX Functions below this line 

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
