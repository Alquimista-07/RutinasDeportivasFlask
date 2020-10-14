import json
from flask import Blueprint, Response, request
ROUTINES = Blueprint('routines', __name__)
TYPE_EXERCISE = Blueprint('type_exercise', __name__)
EXERCISE = Blueprint('exercise', __name__)

from app.models.model_user import User
from app.models.model_type_exercise import Type_Exercise
from app.models.model_exercise import Exercise, BodyPart


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

@TYPE_EXERCISE.route('/createTypeExercise', methods=['POST'])
def create_type_excercise():
    """Create type exercise in database"""
    request_body = request.json
    id_tipo = request_body["id_tipo"]
    dsc_tipo = request_body["dsc_tipo"]
    type_exercise = Type_Exercise(id_tipo_ejercicio=id_tipo, dsc_tipo_ejercicio=dsc_tipo)
    print(type_exercise)
    try:
        type_exercise.save_type_exercise()
        response = Response(status=200, mimetype='application/json')
        return  response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@TYPE_EXERCISE.route('/updateTypeExercise', methods=['PUT'])
def update_type_exercise():
    """Update type exercuse from database"""
    request_body = request.json
    id_tipo = request_body["id_tipo"]
    dsc_tipo = request_body["dsc_tipo"]
    type_exercise_exist = Type_Exercise.get_by_id(id_tipo);
    type_exercise_exist = Type_Exercise(id_tipo_ejercicio=id_tipo, dsc_tipo_ejercicio=dsc_tipo)
    try:
        type_exercise_exist = Type_Exercise.update_type_exercise(type_exercise_exist)
        response = Response(status=200, mimetype='application/json')
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e


@TYPE_EXERCISE.route('/deleteTypeExercise', methods=['DELETE'])
def delete_type_exercise():
    """Delete type exercise from database"""
    request_body = request.json
    id_tipo_ejercicio = request_body['id_tipo_ejercicio']
    try:
        type_exercise = Type_Exercise.get_by_id(id_tipo_ejercicio)
        type_exercise.delete_exercise(type_exercise)
        response = Response(status=200, mimetype='application/json')
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@EXERCISE.route('/createexercise', methods=['POST'])
def create_exercise():
    """Create exercise in database with reltionship"""
    request_body = request.json
    id_ejercicio = request_body['id_ejercicio']
    id_tipo_ejercicio = request_body['id_tipo_ejercicio']
    nombre_ejercicio = request_body['nombre_ejercicio']
    dsc_ejercicio = request_body['dsc_ejercicio']
    bodyPart = BodyPart(id_musculo=9, dsc_musculo="desc")
    exercise = Exercise(id_ejercicio=id_ejercicio, id_tipo_ejercicio=id_tipo_ejercicio, nombre_ejercicio=nombre_ejercicio, dsc_ejercicio=dsc_ejercicio)
    bodyPart.ejercicio.append(exercise)
    exercise.bodyparts.append(bodyPart)
    print(exercise)
    try:
        exercise.save_exercise()
        response = Response(status=200, mimetype='application/json')
        return  response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@EXERCISE.route('/deleteExercise', methods=['DELETE'])
def delete_exercise():
    """Delete exercise from database"""
    required_body = request.json
    id_ejercicio = required_body['id_ejercicio']
    try:
        exercise = Exercise.get_by_id(id_ejercicio)
        exercise.delete_exercise(exercise)
        response = Response(status=200, mimetype='application/json')
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e


@ROUTINES.route('/createbodypart', methods=['POST'])
def create_body_part():
    """Create bodyPart in database"""
    request_body = request.json
    id_musculo = request_body["id_musculo"]
    dsc_musculo = request_body["dsc_musculo"]

    bodyPart = BodyPart(id_musculo=id_musculo, dsc_musculo=dsc_musculo)
    exercise = Exercise(id_ejercicio=10, id_tipo_ejercicio=1,
                        nombre_ejercicio="nombre", dsc_ejercicio="desc")
    bodyPart.ejercicio.append(exercise)
    exercise.bodyparts.append(bodyPart)
    try:
        bodyPart.save_body_part()
        response = Response(status=200, mimetype='application/json')
        return response
    except Exception as exception:
        print('Error : ', exception)
        raise exception