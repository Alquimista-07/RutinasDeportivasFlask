from flask_login import UserMixin
from server import db

class Type_Exercise(db.Model, UserMixin):

    __tablename__ = 'tipo_ejercicio'

    id_tipo_ejercicio = db.Column(db.Integer, primary_key=True)
    dsc_tipo_ejercicio = db.Column(db.String(50), nullable=True)
    exercise = db.relationship("Exercise", backref="tipo_ejercicio")

    def __repr__(self):
        return f'<Type_Exercise {self.id_tipo_ejercicio}, {self.dsc_tipo_ejercicio}>'
