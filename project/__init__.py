from flask import Flask, render_template, request

app = Flask(__name__)

# from blue.api.routes import mod
from project.site.routes import mod

app.register_blueprint(site.routes.mod)
# app.register_blueprint(api.routes.mod, url_prefix='/api')