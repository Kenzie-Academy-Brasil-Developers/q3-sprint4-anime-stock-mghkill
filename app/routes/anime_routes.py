from flask import Flask, Blueprint
from app.controllers import anime_controller


bp = Blueprint("animes", __name__, url_prefix="/api")


bp.get('/animes')(anime_controller.create_anime_controller)

