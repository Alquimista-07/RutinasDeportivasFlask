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
from app.services import load_json_service, specialist_service, \
    registry_service, type_exercise_service, user_service, \
    body_part_service, exercise_service


@ROUTINES.route('/health', methods=['GET', 'OPTIONS'])
def index():
    """Health of application"""
    return Response(json.dumps({'Status': 'OK'}))


@ROUTINES.route('/create', methods=['POST'])
def create_user():
    """Create user in database"""
    request_body = request.json
    user_id = user_service.users_count()
    id_user = user_id + 1
    name = request_body["name"]
    email = request_body["email"]
    password = request_body["password"]
    is_admin = request_body["is_admin"]
    user = User(id=id_user, name=name, email=email, password=password, is_admin=is_admin)
    try:
        user_service.save(user)
        response = json.dumps({"Message" : "Usuario creado satisfactoriamente"}), 200
        return response
    except Exception as exception:
        print('Error : ', exception)
        raise exception


@ROUTINES.route('/updateuser', methods=['PUT'])
def update_user():
    """Update user in database"""
    request_body = request.json
    id_user = request_body["id"]
    name = request_body["name"]
    email = request_body["email"]
    password = request_body["password"]
    is_admin = request_body["is_admin"]
    try:
        user_exists = user_service.get_by_id(id_user)
        if user_exists:
            user_exists = User(id=id_user, name=name, email=email, password=password, is_admin=is_admin)
            user_service.update_user(user_exists)
            response = json.dumps({"Message" : "Usuario actualizado satisfactoriamente"}), 200
            return response
    except Exception as exception:
        print('Error : ', exception)
        raise exception


@ROUTINES.route('/deleteuser', methods=['DELETE'])
def deleteuser():
    """Delete type exercise from database"""
    request_body = request.json
    id = request_body['id']
    try:
        user = user_service.get_by_id(id)
        if user:
            user_service.delete_user(user)
            response = json.dumps({"Message": "Usuario eliminado satisfactoriamente"}), 200
        else:
            response = json.dumps({"Message": "El usuario ingresado no existe"}), 404
        return response
    except Exception as exception:
        print('Error: ', exception)
        raise exception


@TYPE_EXERCISE.route('/createtypeexercise', methods=['POST'])
def create_type_excercise():
    """Create type exercise in database"""
    request_body = request.json
    type_id = type_exercise_service.count_type_exercise()
    id_tipo = type_id + 1
    dsc_tipo = request_body["dsc_tipo"]
    type_exercise = Type_Exercise(id_tipo_ejercicio=id_tipo, dsc_tipo_ejercicio=dsc_tipo)
    try:
        type_exercise_service.save_type_exercise(type_exercise)
        response = json.dumps({"Message": "Tipo de ejercicio creado satisfactoriamente"}), 200
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
        type_exercise_exist = type_exercise_service.get_by_id(id_tipo)
        if type_exercise_exist:
            type_exercise_exist = Type_Exercise(id_tipo_ejercicio=id_tipo, dsc_tipo_ejercicio=dsc_tipo)
            type_exercise_service.update_type_exercise(type_exercise_exist)
            response = json.dumps({"Message": "Tipo de ejercicio actualizado satisfactoriamente"}), 200
        else:
            response = json.dumps({"Message": "El tipo de ejercicio ingresado no existe"}), 404
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
        type_exercise = type_exercise_service.get_by_id(id_tipo_ejercicio)
        if type_exercise:
            type_exercise_service.delete_exercise(type_exercise)
            response = json.dumps({"Message": "Tipo ejercicio eliminado satisfactoriamente"}), 200
        else:
            response = json.dumps({"Message": "El tipo de ejercicio ingresado no existe"}), 404
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
        type_exercise_service.load_archive(ruta)
        response = json.dumps({"Message": "Archivo TXT cargado satisfactoriamente"}), 200
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
    bodyPart = BodyPart(id_musculo=body_part_service.count_body_part() + 1, dsc_musculo="desc")
    exercise = Exercise(id_ejercicio=id_ejercicio, id_tipo_ejercicio=id_tipo_ejercicio, nombre_ejercicio=nombre_ejercicio, dsc_ejercicio=dsc_ejercicio)
    bodyPart.ejercicio.append(exercise)
    exercise.bodyparts.append(bodyPart)
    print(exercise)
    try:
        exercise_service.save_exercise(exercise)
        response = json.dumps({"Message": "Ejercicio creado satisfactoriamente"}), 200
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
        exercise_exists = exercise_service.get_by_id(id_ejercicio)
        if exercise_exists:
            exercise_exists = Exercise(id_ejercicio=id_ejercicio, id_tipo_ejercicio=id_tipo_ejercicio,
                                       nombre_ejercicio=nombre_ejercicio, dsc_ejercicio=dsc_ejercicio)
            exercise_service.update_exercise(exercise_exists)
            response = json.dumps({"Message": "Ejercicio actualizado satisfactoriamente"}), 200
        else:
            response = json.dumps({"Message": "El ejercicio ingresado no existe"}), 404
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
        exercise = exercise_service.get_by_id(id_ejercicio)
        print(exercise)
        if exercise:
            exercise_service.delete_exercise(exercise)
            response = json.dumps({"Message": "Ejercicio eliminado satisfactoriamente"}), 200
        else:
            response = json.dumps({"Message": "El ejercicio ingresado no existe"}), 404
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
        specialist_service.save_specialist(specialist)
        response = json.dumps({"Message": "Especialista creado satisfactoriamente"}), 200
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
        specialist_exists = specialist_service.get_by_id(id_specialist)
        if specialist_exists:
            specialist_exists = Specialist(id_especialista=id_specialist, nombre=name, fecha_nacimiento=birthday_date,
                                           tarjeta_profesional=professional_card)
            specialist_service.update_specialist(specialist_exists)
            response = json.dumps({"Message": "Especialista actualizado satisfactoriamente"}), 200
        else:
            response = json.dumps({"Message": "El especialista ingresado no existe"}), 404
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
        specialist = specialist_service.get_by_id(id_specialist)
        if specialist:
            specialist_service.delete_specialist(specialist)
            response = json.dumps({"Message": "Especialista eliminado satisfactoriamente"}), 200
        else:
            response = json.dumps({"Message": "El especialista ingresado no existe"}), 404
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
        specialist_service.load_archive_csv(ruta)
        response = json.dumps({"Message": "Archivo CSV cargado satisfactoriamente"}), 200
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e


@SPECIALIST.route('/specialistloadmasive', methods=['POST'])
def load_masive_specialist():
    """Load masive data in specialist from archive"""
    request_body = request.json
    ruta = request_body['ruta']
    try:
        load = specialist_service.load_masive(ruta)
        response = json.dumps({"Message" : "Carga Masiva satisfactoriamente", "Time_lapsed" : load})
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
        specialist_service.donwload_json_specialist(dir, file_name)
        response = json.dumps({"Message": "Especialistas descargado a JSON satisfactoriamente"}), 200
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
        registry_service.save_registry(registry)
        response = json.dumps({"Message": "Registro creado satisfactoriamente"}), 200
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
        registry_exists = registry_service.get_by_id(id_registry)
        if registry_exists:
            registry_exists = Registry(id_registro=id_registry, fecha_registro=date_registry)
            registry_service.update_registry(registry_exists)
            response = json.dumps({"Message": "Registro actualizado satisfactoriamente"}), 200
        else:
            response = json.dumps({"Message": "El registro ingresado no existe"}), 404
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
        registry = registry_service.get_by_id(id_registry)
        print("registro", registry)
        if registry:
            registry_service.delete_registry(registry)
            response = json.dumps({"Message": "Registro eliminado satisfactoriamente"}), 200
        else:
            response = json.dumps({"Message": "El registro ingresado no existe"}), 404
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
    exercise = Exercise(id_ejercicio=exercise_service.count_exercise() + 1, id_tipo_ejercicio=1,
                        nombre_ejercicio="nombre", dsc_ejercicio="desc")
    bodyPart.ejercicio.append(exercise)
    exercise.bodyparts.append(bodyPart)
    try:
        body_part_service.save_body_part(bodyPart)
        response = json.dumps({"Message": "Registro parte cuerpo creado satisfactoriamente"}), 200
        return response
    except Exception as exception:
        print('Error : ', exception)
        raise exception


@ROUTINES.route('/createuserfromjson', methods=['POST'])
def create_user_from_json():
    """Create bodyPart in database"""
    load_json_service.create_user_from_json()
    try:
        response = json.dumps({"Message": "Usuario ingresado desde archivo JSON satisfactoriamente"}), 200
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


@ROUTINES.route('/createuserdinamic', methods=['POST'])
def create_user_dinamic():
    """Create user in database from webservice"""
    request_body = request.json
    insert_cant = request_body['insert_cant']
    load_json_service.create_user_dynamic(insert_cant)
    try:
        response = Response(status=200, mimetype='application/json')
        return response
    except Exception as exception:
        print('Error : ', exception)
        raise exception


@ROUTINES.route('/downloadcsvuser', methods=['POST'])
def download_user_csv():
    """Download data user from database to CSV"""
    request_body = request.json
    dir = request_body['ruta']
    file_name = request_body['file_name']
    try:
        user_service.donwload_csv_user(dir, file_name)
        response = json.dumps({"Message": "Usuario descargado a CSV satisfactoriamente"}), 200
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e


@ROUTINES.route('/downloadtxtuser', methods=['POST'])
def download_user_txt():
    """Download data user from database to CSV"""
    request_body = request.json
    dir = request_body['ruta']
    file_name = request_body['file_name']
    try:
        user_service.download_txt_user(dir, file_name)
        response = json.dumps({"Message": "Usuario descargado a TXT satisfactoriamente"}), 200
        return response
    except Exception as e:
        print('Error causado por: ', e)
        raise e

