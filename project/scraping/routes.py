from flask import Blueprint, Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
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
        gameTitle = fix_String.transform_user_input_to_lowercase(gameTitle)
        gameTitle = fix_String.add_dash_in_gameTitle(gameTitle)
        review_grades = scrape.get_data_based_on_game_title(gameTitle, gameSystem)
        # print(review_grades)
        #Need to convert my list to a DF or Series 
        #Need to calculate the mean from that
        #Need to calculate the standard deviavtion 
        #Need to make a bar graph of the scores. 
    return render_template('scraping/scraping.html')