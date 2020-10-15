from flask_login import UserMixin
from server import db

import numpy as np
from time import time
import json
import os

def Load_Data(file_name):
    data = np.genfromtxt(file_name, delimiter=';', names=True, dtype=None)
    return data.tolist()

class Specialist(db.Model, UserMixin):

    __tablename__ = 'especialista'

    id_especialista = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=False)
    tarjeta_profesional = db.Column(db.String(12), nullable=False)
    registry = db.relationship("Registry", uselist=False, backref="especialista", cascade="all,delete")

    def __repr__(self):
        return f'<Specialist {self.id_especialista}, {self.nombre}, {self.fecha_nacimiento}>'

    def save_specialist(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id_especialista):
        return Specialist.query.get(id_especialista)

    @staticmethod
    def update_specialist(specialist):
        db.session.merge(specialist)
        db.session.commit()
        db.session.close()

    @staticmethod
    def delete_specialist(specialist):
        db.session.delete(specialist)
        db.session.commit()
        db.session.close()

    @staticmethod
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


    @staticmethod
    def donwload_json_specialist(dir, file_name):
        data = db.session.query(Specialist)
        dir = dir
        file_name = file_name
        for specialist in data:
            record = specialist.id_especialista, specialist.nombre, specialist.fecha_nacimiento.strftime('%Y-%m-%d'), specialist.tarjeta_profesional
            format_json = json.dumps({
                "id_specialist": record[0],
                "name": record[1],
                "birthday_date": record[2],
                "professional_card": record[3]
            }, separators=(",", ":"))

            with open(os.path.join(dir, file_name), 'a') as file:
                file.write(format_json +'\n')
        db.session.close()

    @staticmethod
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
