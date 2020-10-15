import json
from app.models.model_user import User

def create_user_from_json():
    my_file = open('app/services/load_json_service.py')
    data = json.load(my_file)

    for values in data['data']:
        id_user = values["id"]
        name = values["name"]
        email = values["email"]
        password = values["password"]
        is_admin = values["is_admin"]
        user = User(id=id_user, name=name, email=email, password=password, is_admin=is_admin)
        user.save()
        print(user)
    my_file.close()


