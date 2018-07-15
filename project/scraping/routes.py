from flask import Blueprint, Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash

mod = Blueprint('scraping', __name__, template_folder='templates', static_folder='static',
                                                static_url_path='/static')

@mod.route('/scraping_home', methods=['GET', 'POST'])
def scraping_homepage():
    if request.method == 'POST':
        #Recieving the information from the user.
        gameTitle = request.form['gameTitle']
        print(gameTitle)
    return render_template('scraping/scraping.html')