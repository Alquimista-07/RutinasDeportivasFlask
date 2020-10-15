import numpy as np
from time import time
from server import db
from app.models.model_type_exercise import Type_Exercise


def Load_Data(file_name):
    data = np.genfromtxt(file_name, delimiter='|', names=True, dtype=None)
    return data.tolist()

def save_type_exercise(self):
    db.session.add(self)
    db.session.commit()

def get_by_id(id_tipo):
    return Type_Exercise.query.get(id_tipo)

def update_type_exercise(type_exercise):
    db.session.merge(type_exercise)
    db.session.commit()
    db.session.close()

def delete_exercise(type_exercise):
    db.session.delete(type_exercise)
    db.session.commit()
    db.session.close()

def load_archive(ruta):
    tiempo = time()
    try:
        file_name = ruta
        data = Load_Data(file_name)

        for row in data:
            record = Type_Exercise(**{
                'id_tipo_ejercicio': row[0],
                'dsc_tipo_ejercicio': row[1]
            })
            db.session.add(record)
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()
        print("Tiempo transcurrido: " + str(time() - tiempo) + " s.")
