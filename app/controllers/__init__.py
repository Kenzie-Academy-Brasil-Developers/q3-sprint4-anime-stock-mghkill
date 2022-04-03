from http import HTTPStatus


def detect_key_error(data):
    keys = [  
            "anime",
            "realeased_date",
            "seasons"
    ]
    
    error = ""

    key_error = list(data.keys())

    for key in key_error:
        if not key in keys:
            error = key

    return  {
                "available_keys": [
                    "anime",
                    "released_date",
                    "seasons"
                ],
                "wrong_keys_sended": [
                    error
                ]
            }, HTTPStatus.UNPROCESSABLE_ENTITY

