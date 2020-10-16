from server import db

import numpy as np
from app.models.model_specialist import Specialist
from time import time
import json
import os

def Load_Data(file_name):
    data = np.genfromtxt(file_name, delimiter=';', names=True, dtype=None)
    return data.tolist()

def save_specialist(self):
    db.session.add(self)
    db.session.commit()


def get_by_id(id_especialista):
    return Specialist.query.get(id_especialista)


def update_specialist(specialist):
    db.session.merge(specialist)
    db.session.commit()
    db.session.close()


def delete_specialist(specialist):
    db.session.delete(specialist)
    db.session.commit()
    db.session.close()


def count_specialist():
    return Specialist.query.count()

def load_archive_csv(ruta):
    tiempo = time()
    try:
        file_name = ruta
        data = Load_Data(file_name)

        for row in data:
            record = Specialist(**{
                'id_especialista': row[0],
                'nombre': row[1],
                'fecha_nacimiento': row[2],
                'tarjeta_profesional': row[3]
            })
            db.session.add(record)
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()
        print("Tiempo transcurrido: " + str(time() - tiempo) + " s.")


def donwload_json_specialist(dir, file_name):
    data = db.session.query(Specialist)
    dir = dir
    file_name = file_name
    increment = 0
    start_json = '{ "data": ['
    end_json = ''
    separador = ','
    for specialist in data:
        increment = increment + 1
        record = specialist.id_especialista, specialist.nombre, specialist.fecha_nacimiento.strftime(
            '%Y-%m-%d'), specialist.tarjeta_profesional
        format_json = json.dumps({
            "id_specialist": record[0],
            "name": record[1],
            "birthday_date": record[2],
            "professional_card": record[3]
        }, separators=(",", ":"))

        if increment > 1:
            start_json = ''

        if increment == count_specialist():
            end_json = '] }'
            separador = ''

        with open(os.path.join(dir, file_name), 'a') as file:
            file.write(start_json + format_json + end_json + separador + '\n')
    db.session.close()


def load_masive(ruta):
    tiempo = time()
    try:
        file_name = ruta
        data = Load_Data(file_name)

        for row in data:
            record = Specialist(**{
                'id_especialista': row[0],
                'nombre': row[1],
                'fecha_nacimiento': row[2],
                'tarjeta_profesional': row[3]
            })
            db.session.add(record)
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()
        response = str(time() - tiempo) + " s."
        return response