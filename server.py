from flask import Flask
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__, instance_relative_config=True)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/rutinas'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(APP)
from app.controllers.rutinas_controller import ROUTINES
APP.register_blueprint(ROUTINES)


@APP.errorhandler(Exception)
def handle_exception(error):
    print(error)
    return exceptions.InternalServerError()


if __name__ == '__main__':
    print("Starting server")
    APP.run(host='0.0.0.0', port=5001, debug=True)
