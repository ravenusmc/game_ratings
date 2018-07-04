from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash

app = Flask(__name__)

from project.csv_data.routes import mod
from project.site.routes import mod
from project.scraping.routes import mod

app.register_blueprint(site.routes.mod)
app.register_blueprint(csv_data.routes.mod)
app.register_blueprint(scraping.routes.mod)
