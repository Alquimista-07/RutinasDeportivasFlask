from flask_login import UserMixin
from server import db


class Type_Exercise(db.Model, UserMixin):

    __tablename__ = 'tipo_ejercicio'

    id_tipo_ejercicio = db.Column(db.Integer, primary_key=True)
    dsc_tipo_ejercicio = db.Column(db.String(50), nullable=True)
    exercise = db.relationship('Exercise', back_populates="type_exercise")

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
        if not type_exercise:
            db.session.merge(type_exercise)
            db.session.commit()
            db.session.close()
        else:
            print('El tipo de ejercicio ingresado no existe')

    @staticmethod
    def delete_exercise(type_exercise):
        db.session.delete(type_exercise)
        db.session.commit()
        db.session.close()
