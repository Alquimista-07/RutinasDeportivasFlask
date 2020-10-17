from app.models.model_exercise import BodyPart
from server import db


def count_body_part():
    return BodyPart.query.count()


def save_body_part(self):
    db.session.add(self)
    db.session.commit()