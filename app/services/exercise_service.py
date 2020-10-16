from app.models.model_exercise import Exercise


def count_exercise():
    return Exercise.query.count()

