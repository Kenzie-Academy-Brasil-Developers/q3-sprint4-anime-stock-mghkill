from flask import Flask
from .anime_routes import bp as bp_anime
from .anime_routes import bp_animes
def init_app(app: Flask):
    
    app.register_blueprint(bp_animes)
    app.register_blueprint(bp_anime)
    