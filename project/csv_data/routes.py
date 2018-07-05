from flask import Blueprint, Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
from project.csv_data.data import * 

mod = Blueprint('csv_data', __name__,template_folder='templates', static_folder='static',
                                                static_url_path='/static')

@mod.route('/csv_home')
def homepage():
  return render_template('csv_data/csv_index.html')


#AJAX Functions below this line 

#This route will deal with getting the max rating of a video game by year and genre 
@mod.route('/_by_max_rating')
def by_state_shape():
    year = request.args.get('year', 0, type=int)
    genre = request.args.get('genre', 0, type=str)
    result = genre
    return jsonify(result = result)
