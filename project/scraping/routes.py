from flask import Blueprint, Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
import json 
from project.scraping.scraping import *
from project.scraping.fixInput import *

mod = Blueprint('scraping', __name__, template_folder='templates', static_folder='static',
                                                static_url_path='/static')

@mod.route('/scraping_home', methods=['GET', 'POST'])
def scraping_homepage():
    if request.method == 'POST':
        #Creating the objects that I'll use in this route
        fix_String = Fix_Input()
        scrape = Web_Scraping()
        #Recieving the information from the user.
        gameTitle = request.form['gameTitle']
        gameSystem = request.form['system']

        game_Title = gameTitle 

        gameTitle = fix_String.transform_user_input_to_lowercase(gameTitle)
        gameTitle = fix_String.add_dash_in_gameTitle(gameTitle)

        review_grades = scrape.get_data_based_on_game_title(gameTitle, gameSystem)

        if review_grades == 'No Data Found!':
            score_mean_formatted = review_grades
            score_median_formatted = review_grades
            score_std_formatted = review_grades
        else:
            score_dataFrame = scrape.convert_list_to_series(review_grades)
            score_mean_formatted = scrape.calculate_mean(score_dataFrame)
            score_std_formatted = scrape.calculate_standard_deviation(score_dataFrame)
            score_median_formatted = scrape.calculate_median(score_dataFrame)
        return render_template('scraping/scraping.html', mean = json.dumps(score_mean_formatted), 
            std = json.dumps(score_std_formatted), scores = json.dumps(review_grades), game_title = game_Title,
            median = json.dumps(score_median_formatted))
    return render_template('scraping/scraping.html')
































