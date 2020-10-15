import json
from flask import Blueprint, Response, request
ROUTINES = Blueprint('routines', __name__)
TYPE_EXERCISE = Blueprint('type_exercise', __name__)
EXERCISE = Blueprint('exercise', __name__)
SPECIALIST = Blueprint('specialist', __name__)
REGISTRY = Blueprint('registry', __name__)

from app.models.model_user import User
from app.models.model_type_exercise import Type_Exercise
from app.models.model_exercise import Exercise, BodyPart

from app.models.model_exercise import Exercise
from app.models.model_specialist import Specialist
from app.models.model_registry import Registry
from app.services import load_json_service

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

@TYPE_EXERCISE.route('/createtypeexercise', methods=['POST'])
def create_type_excercise():
    """Create type exercise in database"""
    request_body = request.json
    id_tipo = request_body["id_tipo"]
    dsc_tipo = request_body["dsc_tipo"]
    type_exercise = Type_Exercise(id_tipo_ejercicio=id_tipo, dsc_tipo_ejercicio=dsc_tipo)
    print(type_exercise)
    try:
        type_exercise.save_type_exercise()
        response = Response(status=200, mimetype='application/json', response='Tipo de ejercicio creado satisfactoriamente')
        return  response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@TYPE_EXERCISE.route('/updatetypeexercise', methods=['PUT'])
def update_type_exercise():
    """Update type exercuse from database"""
    request_body = request.json
    id_tipo = request_body["id_tipo"]
    dsc_tipo = request_body["dsc_tipo"]
    try:
        type_exercise_exist = Type_Exercise.get_by_id(id_tipo)
        if type_exercise_exist:
            type_exercise_exist = Type_Exercise(id_tipo_ejercicio=id_tipo, dsc_tipo_ejercicio=dsc_tipo)
            Type_Exercise.update_type_exercise(type_exercise_exist)
            response = Response(status=200, mimetype='application/json', response='Tipo de ejercicio actualizado satisfactoriamente')
        else:
            response = Response(status=406, mimetype='application/json', response='El tipo de ejercicio ingresado no existe')
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e


@TYPE_EXERCISE.route('/deletetypeexercise', methods=['DELETE'])
def delete_type_exercise():
    """Delete type exercise from database"""
    request_body = request.json
    id_tipo_ejercicio = request_body['id_tipo_ejercicio']
    try:
        type_exercise = Type_Exercise.get_by_id(id_tipo_ejercicio)
        if type_exercise:
            type_exercise.delete_exercise(type_exercise)
            response = Response(status=200, mimetype='application/json', response='Tipo ejercicio eliminado satisfactoriamente')
        else:
            response = Response(status=406, mimetype='application/json', response='El tipo de ejercicio ingresado no existe')
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@TYPE_EXERCISE.route('/exercisetypeload', methods=['POST'])
def load_type_exercise():
    """Load data in type excercise from txt"""
    request_body = request.json
    ruta = request_body['ruta']
    try:
        type_exersice = Type_Exercise()
        type_exersice.load_archive(ruta)
        response = Response(status=200, mimetype='application/json', response='Archivo TXT cargado satisfactoriamente')
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
        response = Response(status=200, mimetype='application/json', response='Ejercicio creado satisfactoriamente')
        return  response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@EXERCISE.route('/updateexercise', methods=['PUT'])
def update_exercise():
    """Update exercise in database with reltionship"""
    request_body = request.json
    id_ejercicio = request_body['id_ejercicio']
    id_tipo_ejercicio = request_body['id_tipo_ejercicio']
    nombre_ejercicio = request_body['nombre_ejercicio']
    dsc_ejercicio = request_body['dsc_ejercicio']
    try:
        exercise_exists = Exercise.get_by_id(id_ejercicio)
        if exercise_exists:
            exercise_exists = Exercise(id_ejercicio=id_ejercicio, id_tipo_ejercicio=id_tipo_ejercicio,
                                       nombre_ejercicio=nombre_ejercicio, dsc_ejercicio=dsc_ejercicio)
            exercise_exists.update_exercise(exercise_exists)
            response = Response(status=200, mimetype='application/json', response='Ejercicio actualizado satisfactoriamente')
        else:
            response = Response(status=406, mimetype='application/json', response='El ejercicio ingresado no existe')
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@EXERCISE.route('/deleteexercise', methods=['DELETE'])
def delete_exercise():
    """Delete exercise from database"""
    required_body = request.json
    id_ejercicio = required_body['id_ejercicio']
    try:
        exercise = Exercise.get_by_id(id_ejercicio)
        if exercise:
            exercise.delete_exercise(exercise)
            response = Response(status=200, mimetype='application/json', response='Ejercicio eliminado satisfactoriamente')
        else:
            response = Response(status=406, mimetype='application/json', response='El ejercicio ingresado no existe')
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@SPECIALIST.route('/createspecialist', methods=['POST'])
def create_specialist():
    """Create Specialist in database"""
    request_body = request.json
    with_registry = request_body["with_registry"]
    id_specialist = request_body["id_specialist"]
    name = request_body["name"]
    birthday_date = request_body["birthday_date"]
    professional_card = request_body["professional_card"]
    specialist = Specialist(id_especialista=id_specialist, nombre=name, fecha_nacimiento=birthday_date,
                            tarjeta_profesional=professional_card)
    #---------------
    if with_registry:
        id_registry = request_body["id_registry"]
        date_regitry = request_body["date_registry"]

        registry = Registry(id_registro=id_registry, fecha_registro=date_regitry)
        specialist.registry = registry
    # ---------------
    try:
        specialist.save_specialist()
        response = Response(status=200, mimetype='application/json', response='Especialista creado satisfactoriamente')
        return  response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@SPECIALIST.route('/updatespecialist', methods=['PUT'])
def update_specialist():
    """Update specialist in database with reltionship"""
    request_body = request.json
    id_specialist = request_body["id_specialist"]
    name = request_body["name"]
    birthday_date = request_body["birthday_date"]
    professional_card = request_body["professional_card"]
    try:
        specialist_exists = Specialist.get_by_id(id_specialist)
        if specialist_exists:
            specialist_exists = Specialist(id_especialista=id_specialist, nombre=name, fecha_nacimiento=birthday_date,
                                           tarjeta_profesional=professional_card)
            specialist_exists.update_specialist(specialist_exists)
            response = Response(status=200, mimetype='application/json', response='Especialista actualizado satisfactoriamente')
        else:
            response = Response(status=406, mimetype='application/json', response='El especialista ingresado no existe')
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@SPECIALIST.route('/deletespecialist', methods=['DELETE'])
def delete_specialist():
    """Delete specialist from database"""
    required_body = request.json
    id_specialist = required_body['id_specialist']
    try:
        specialist = Specialist.get_by_id(id_specialist)
        if specialist:
            specialist.delete_specialist(specialist)
            response = Response(status=200, mimetype='application/json', response='Especialista eliminado satisfactoriamente')
        else:
            response = Response(status=406, mimetype='application/json', response='El especialista ingresado no existe')
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e


@SPECIALIST.route('/specialistload', methods=['POST'])
def load_specialist():
    """Load data in specialist from csv"""
    request_body = request.json
    ruta = request_body['ruta']
    try:
        specialist = Specialist()
        specialist.load_archive_csv(ruta)
        response = Response(status=200, mimetype='application/json', response='Archivo CSV cargado satisfactoriamente')
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@SPECIALIST.route('/downloadspecialistjson', methods=['POST'])
def list_specialist():
    """Download data specialist from database to JSON"""
    request_body = request.json
    dir = request_body['ruta']
    file_name = request_body['file_name']
    try:
        specialist = Specialist()
        specialist.donwload_json_specialist(dir, file_name)
        response = Response(status=200, mimetype='application/json', response='Especialistas descargado a JSON satisfactoriamente')
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e


@REGISTRY.route('/createregistry', methods=['POST'])
def create_registry():
    """Create registry in database"""
    request_body = request.json
    id_registry = request_body["id_registry"]
    date_registry = request_body["date_registry"]
    registry = Registry(id_registro=id_registry, fecha_registro=date_registry)
    print(registry)
    try:
        registry.save_registry()
        response = Response(status=200, mimetype='application/json', response='Registro creado satisfactoriamente')
        return  response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@REGISTRY.route('/updateregistry', methods=['PUT'])
def update_registry():
    """Update registry in database with reltionship"""
    request_body = request.json
    id_registry = request_body["id_registry"]
    date_registry = request_body["date_registry"]
    try:
        registry_exists = Registry.get_by_id(id_registry)
        if registry_exists:
            registry_exists = Registry(id_registro=id_registry, fecha_registro=date_registry)
            registry_exists.update_registry(registry_exists)
            response = Response(status=200, mimetype='application/json', response='Registro actualizado satisfactoriamente')
        else:
            response = Response(status=406, mimetype='application/json', response='El registro ingresado no existe')
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

@REGISTRY.route('/deleteregistry', methods=['DELETE'])
def delete_registy():
    """Delete registry from database"""
    request_body = request.json
    id_registry = request_body['id_registry']
    try:
        registry = Registry.get_by_id(id_registry)
        print("registro", registry)
        if registry:
            registry.delete_registry(registry)
            response = Response(status=200, mimetype='application/json', response='Registro eliminado satisfactoriamente')
        else:
            response = Response(status=406, mimetype='application/json', response='El registro ingresado no existe')
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


@ROUTINES.route('/createuserfromjson', methods=['POST'])
def create_user_from_json():
    """Create bodyPart in database"""
    load_json_service.create_user_from_json()
    try:
        response = Response(status=200, mimetype='application/json')
        return response
    except Exception as exception:
        print('Error : ', exception)
        raise exception


@ROUTINES.route('/createuserfromwebservice', methods=['POST'])
def create_user_from_web_service():
    """Create user in database from webservice"""
    load_json_service.create_user_from_web_service()
    try:
        response = Response(status=200, mimetype='application/json')
        return response
    except Exception as exception:
        print('Error : ', exception)
        raise exception