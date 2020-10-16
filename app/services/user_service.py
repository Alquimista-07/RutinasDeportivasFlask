import string
import random
from werkzeug.security import generate_password_hash, check_password_hash
from server import db
from app.models.model_user import User
import csv


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


def users_count():
    return User.query.count()


def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def donwload_csv_user(dir, file_name):
    try:
        data = db.session.query(User)
        archive = dir + file_name
        output_csv = open(archive, 'w')
        fields = ['id', 'name', 'email', 'password', 'is_admin']
        output = csv.DictWriter(output_csv, delimiter=';', lineterminator='\n', fieldnames=fields)
        output.writeheader()
        for user in data:
            output.writerow({'id': user.id, 'name': user.name, 'email': user.email, 'password': user.password, 'is_admin': user.is_admin})
    finally:
        output_csv.close()


def download_txt_user(dir, file_name):
    try:
        data = db.session.query(User)
        archive = dir + file_name
        file = open(archive, 'w')
        for user in data:
            record = [user.id, user.name, user.email, user.password, user.is_admin]
            file.write(str(record)[1:-1] + '\n')
    finally:
        file.close()