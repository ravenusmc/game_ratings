from flask import Blueprint, render_template
from project.csv_data.data import * 

mod = Blueprint('csv_data', __name__,template_folder='templates', static_folder='static',
                                                static_url_path='/static')

@mod.route('/csv_home')
def homepage():
  return render_template('csv_data/csv_index.html')
