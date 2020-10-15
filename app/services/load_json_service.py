import json
import requests
from app.models.model_user import User
from app.services import user_service

def create_user_from_json():
    my_file = open('app/resource/dataUsers.json')
    data = json.load(my_file)

    for values in data['data']:
        id_user = values["id"]
        name = values["name"]
        email = values["email"]
        password = values["password"]
        is_admin = values["is_admin"]
        user = User(id=id_user, name=name, email=email, password=password, is_admin=is_admin)
        user_service.save(user)
        print(user)
    my_file.close()


def create_user_from_web_service():
    response_webservice = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
    data = json.loads(response_webservice.text)
    user_id = 100
    for values in data['game_indices']:
        print(values['version'].get('name'))
        user_id += 1
        id_user = user_id
        name = values["version"].get('name')
        email = values["version"].get('url')
        password = "password"
        is_admin = True
        user = User(id=id_user, name=name, email=email, password=password, is_admin=is_admin)
        user_service.save(user)


