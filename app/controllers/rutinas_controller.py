import json
from flask import Blueprint, Response, request
ROUTINES = Blueprint('routines', __name__)
from app.models.model_user import User

@ROUTINES.route('/health', methods=['GET', 'OPTIONS'])
def index():
    """Health of application"""
    return Response(json.dumps({'Status': 'OK'}))


@ROUTINES.route('/create', methods=['POST'])
def create_user():
    """Create user in database"""
    request_body = request.json
    id_user = request_body["id"]
    name = request_body["name"]
    email = request_body["email"]
    password = request_body["password"]
    is_admin = request_body["is_admin"]
    user = User(id=id_user, name=name, email=email, password=password, is_admin=is_admin)
    try:
        user.save()
        response = Response(status=200, mimetype='application/json')
        return response
    except Exception as exception:
        print('Error : ', exception)
        raise exception