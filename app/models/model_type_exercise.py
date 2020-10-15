from flask_login import UserMixin
from server import db

import numpy as np
from time import time

def Load_Data(file_name):
    data = np.genfromtxt(file_name, delimiter='|', names=True, dtype=None)
    return data.tolist()

class Type_Exercise(db.Model, UserMixin):

    __tablename__ = 'tipo_ejercicio'

    id_tipo_ejercicio = db.Column(db.Integer, primary_key=True)
    dsc_tipo_ejercicio = db.Column(db.String(50), nullable=True)
    exercise = db.relationship("Exercise", backref="tipo_ejercicio")

    def __repr__(self):
        return f'<Type_Exercise {self.id_tipo_ejercicio}, {self.dsc_tipo_ejercicio}>'

    def save_type_exercise(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id_tipo):
        return Type_Exercise.query.get(id_tipo)

    @staticmethod
    def update_type_exercise(type_exercise):
        db.session.merge(type_exercise)
        db.session.commit()
        db.session.close()

    @staticmethod
    def delete_exercise(type_exercise):
        db.session.delete(type_exercise)
        db.session.commit()
        db.session.close()

    @staticmethod
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
