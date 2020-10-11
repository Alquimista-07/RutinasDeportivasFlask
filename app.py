import json
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/rutinas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from models import User


@app.route('/health', methods=['GET', 'OPTIONS'])
def index():
    """Health of application"""
    return Response(json.dumps({'Status': 'OK'}))


@app.route('/create', methods=['POST'])
def create_user():
    """Create user in database"""
    request_body = request.json
    id = request_body["id"]
    name = request_body["name"]
    email = request_body["email"]
    password = request_body["password"]
    is_admin = request_body["is_admin"]
    user = User(id=id, name=name, email=email, password=password, is_admin=is_admin)
    try:
        user.save()
        response = Response(status=200, mimetype='application/json')
        return response
    except Exception as exception:
        print('Error : %s', exception)
        raise exception


if __name__ == '__main__':
    app.run()
