from flask import Blueprint
from app.controllers import anime_controller

bp = Blueprint("animes", __name__, url_prefix="/animes")
bp_animes = Blueprint("delete", __name__, url_prefix="/delete")


bp.post('')(anime_controller.create_anime_controller)
bp.get('')(anime_controller.get_anime_controller)
bp.get('/<int:anime_id>')(anime_controller.get_by_id_controller)
bp.patch('/<int:anime_id>')(anime_controller.update_by_id_controller)
bp_animes.delete('/<int:anime_id>')(anime_controller.delete_by_id_controller)


