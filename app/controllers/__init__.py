from http import HTTPStatus


def detect_key_error(data):
    keys = [  
            "anime",
            "released_date",
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

def detect_key_error_patch(data):
    keys = [  
        "anime",
        "released_date",
        "seasons"
    ]

    key_error = list(data.keys())
    print(key_error)

    for key in key_error:
        if not key in keys:
            return  {
                "available_keys": [
                    "anime",
                    "released_date",
                    "seasons"
                ],
                "wrong_keys_sended": [
                    key
                ]
            }, HTTPStatus.UNPROCESSABLE_ENTITY
    return {}