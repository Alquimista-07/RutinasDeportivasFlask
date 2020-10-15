from server import db
from app.models.model_registry import Registry

def save_registry(self):
    db.session.add(self)
    db.session.commit()


def get_by_id(id_registro):
    return Registry.query.get(id_registro)


def update_registry(registry):
    db.session.merge(registry)
    db.session.commit()
    db.session.close()


def delete_registry(registry):
    db.session.delete(registry)
    db.session.commit()
    db.session.close()