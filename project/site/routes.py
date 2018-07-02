from flask import Blueprint, render_template

mod = Blueprint('site', __name__,template_folder='templates')
mod = Blueprint('site', __name__,static_folder='templates')

@mod.route('/')
def homepage():
  return render_template('site/index.html')