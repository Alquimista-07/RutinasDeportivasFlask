from flask_login import UserMixin
from server import db

class Exercise(db.Model, UserMixin):

    __tablename__ = 'ejercicio'

    id_ejercicio = db.Column(db.Integer, primary_key=True)
    id_tipo_ejercicio = db.Column(db.Integer, db.ForeignKey('tipo_ejercicio.id_tipo_ejercicio'))
    nombre_ejercicio = db.Column(db.String(50), nullable=True)
    dsc_ejercicio = db.Column(db.String(200), nullable=True)
    type_exercise = db.relationship("Type_Exercise", back_populates="exercise", cascade="all,delete")

    def __repr__(self):
        return f'<Exercise {self.id_ejercicio}, {self.id_tipo_ejercicio}, {self.nombre_ejercicio}, {self.dsc_ejercicio}>'

    def save_exercise(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id_ejercicio):
        return Exercise.query.get(id_ejercicio)

    @staticmethod
    def update_exercise(exercise):
        if not exercise:
            db.session.merge(exercise)
            db.session.commit()
            db.session.close()
        else:
            print('El ejercicio ingresado no existe')

    @staticmethod
    def delete_exercise(exercise):
        db.session.delete(exercise)
        db.session.commit()
        db.session.close()
