from flask import Blueprint, render_template
from project.site.test import *

mod = Blueprint('site', __name__,template_folder='templates', static_folder='static',
                                                static_url_path='/static')

@mod.route('/')
def homepage():
  test = Test()
  name = test.test()
  return render_template('site/index.html', name = name)

@mod.route('/home')
def home():
    return render_template('site/home.html')