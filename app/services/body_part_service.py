from app.models.model_exercise import BodyPart


def count_body_part():
    return BodyPart.query.count()

