from app.models.model_exercise import Exercise
from server import db


def count_exercise():
    return Exercise.query.count()


def save_exercise(self):
    db.session.add(self)
    db.session.commit()


def get_by_id(id_ejercicio):
    return Exercise.query.get(id_ejercicio)


def update_exercise(exercise):
    db.session.merge(exercise)
    db.session.commit()
    db.session.close()


def delete_exercise(exercise):
    db.session.delete(exercise)
    db.session.commit()
    db.session.close()
