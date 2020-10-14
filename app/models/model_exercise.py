from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship
from server import db


musculo_ejercicio = db.Table('musculo_ejercicio',
    db.Column('id_musculo', db.Integer, db.ForeignKey('parte_cuerpo.id_musculo')),
    db.Column('id_ejercicio', db.Integer, db.ForeignKey('ejercicio.id_ejercicio'))
)


class Exercise(db.Model, UserMixin):

    __tablename__ = 'ejercicio'

    id_ejercicio = db.Column(db.Integer, primary_key=True)
    id_tipo_ejercicio = db.Column(db.Integer, db.ForeignKey('tipo_ejercicio.id_tipo_ejercicio'))
    nombre_ejercicio = db.Column(db.String(50), nullable=True)
    dsc_ejercicio = db.Column(db.String(200), nullable=True)
    type_exercise = db.relationship("Type_Exercise", back_populates="exercise", cascade="all,delete")
    bodyparts = relationship("BodyPart",  secondary=musculo_ejercicio, back_populates="ejercicio", lazy='dynamic')

    def __repr__(self):
        return f'<Exercise {self.id_ejercicio}, {self.id_tipo_ejercicio}, {self.nombre_ejercicio}, {self.dsc_ejercicio}>'

    def save_exercise(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id_ejercicio):
        return Exercise.query.get(id_ejercicio)

    @staticmethod
    def update_exercise():
        db.session.update()
        db.session.commit()
        db.session.close()

    @staticmethod
    def delete_exercise(exercise):
        db.session.delete(exercise)
        db.session.commit()
        db.session.close()


class BodyPart(db.Model, UserMixin):

    __tablename__ = 'parte_cuerpo'

    id_musculo = db.Column(db.Integer, primary_key=True)
    #par_id_musculo = db.column(db.Integer, )
    dsc_musculo = db.Column(db.String(50), nullable=False)
    ejercicio = relationship("Exercise", secondary=musculo_ejercicio, back_populates="bodyparts")

    def __repr__(self):
        return f'<BodyPart {self.id_musculo}, {self.desc_musculo}>'

    def save_body_part(self):
        db.session.add(self)
        db.session.commit()
