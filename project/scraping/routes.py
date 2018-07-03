from flask import Blueprint, render_template

mod = Blueprint('scraping', __name__, template_folder='templates', static_folder='static',
                                                static_url_path='/static')

@mod.route('/scraping_home')
def scraping_homepage():
  return render_template('scraping/scraping.html')