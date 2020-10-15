from flask_login import UserMixin
from server import db

class Specialist(db.Model, UserMixin):

    __tablename__ = 'especialista'

    id_especialista = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=False)
    tarjeta_profesional = db.Column(db.String(12), nullable=False)
    registry = db.relationship("Registry", uselist=False, backref="especialista", cascade="all,delete")

    def __repr__(self):
        return f'<Specialist {self.id_especialista}, {self.nombre}, {self.fecha_nacimiento}>'

