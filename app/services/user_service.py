from werkzeug.security import generate_password_hash, check_password_hash
from server import db
from app.models.model_user import User


def set_password(self, password):
    self.password = generate_password_hash(password)


def check_password(self, password):
    return check_password_hash(self.password, password)


def save(self):
    db.session.add(self)
    db.session.commit()


def get_by_id(id):
    return User.query.get(id)


def get_by_email(email):
    return User.query.filter_by(email=email).first()


def update_user(user):
    db.session.merge(user)
    db.session.commit()
    db.session.close()


def delete_user(user):
    db.session.delete(user)
    db.session.commit()
    db.session.close()
