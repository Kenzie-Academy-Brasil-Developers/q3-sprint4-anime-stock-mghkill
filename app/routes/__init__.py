from flask import Flask
from .anime_routes import bp as bp_anime

def init_app(app: Flask):

    app.register_blueprint(bp_anime)