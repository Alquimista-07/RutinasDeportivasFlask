from flask_login import UserMixin
from server import db

class Registry(db.Model, UserMixin):

    __tablename__ = 'registro'

    id_registro = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), primary_key=True)
    fecha_registro = db.Column(db.DateTime, nullable=True)
    specialist = db.relationship("Specialist", back_populates="registry")

    def __repr__(self):
        return f'<Registry {self.id_registro}, {self.fecha_registro}>'

