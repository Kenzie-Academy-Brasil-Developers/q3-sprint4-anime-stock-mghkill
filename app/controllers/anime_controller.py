from curses.ascii import HT
from http import HTTPStatus
from flask import request
from psycopg2.errors import UniqueViolation
from app.controllers import detect_key_error, detect_key_error_patch
from app.models.anime_models import Anime



def create_anime_controller():
    Anime.create_table()
    data = request.get_json()
       
    try:
        animes = Anime(**data)
    except KeyError:
        return detect_key_error(data)
    
    try:
        inserted_anime = animes.create_anime()
    except UniqueViolation:
        return {"error": "This anime already exists"}, HTTPStatus.UNPROCESSABLE_ENTITY
    serialized_anime = Anime.serialize(inserted_anime)

    return serialized_anime , HTTPStatus.CREATED




def get_anime_controller():

    Anime.create_table()

    anime = Anime.get_animes()

    output = [Anime.serialize(element) for element in anime]

    return {"data": output}, HTTPStatus.OK



def get_by_id_controller(anime_id):
    Anime.create_table()

    anime = Anime.get_animes()

    output = [Anime.serialize(element) for element in anime]

    output_filtered = ""

    for item in output:
        if int(item["id"]) == int(anime_id):
            output_filtered = item

    if not output_filtered:
        return {"message": "Not Found"}, HTTPStatus.NOT_FOUND

    return {"data": output_filtered}, HTTPStatus.OK





def update_by_id_controller(anime_id):
    data = request.get_json()

    detect_error = detect_key_error_patch(data)

    if detect_error:
        return detect_error


    updated_animes = Anime.update_animes(anime_id, data)

    if not updated_animes:
        return {"error": "Not Found"}, HTTPStatus.NOT_FOUND

    serialized_user = Anime.serialize(updated_animes)

    return {"data": serialized_user}
    





def delete_by_id_controller(anime_id):

    Anime.create_table()
   
    anime = Anime.get_animes()

    output = [Anime.serialize(element) for element in anime]

    output_filtered = ""

    for item in output:
        if int(item["id"]) == int(anime_id):
            output_filtered = item

    if not output_filtered:
        return {"message": "Not Found"}, HTTPStatus.NOT_FOUND

    Anime.delete_animes(anime_id)

    return "", HTTPStatus.NO_CONTENT
