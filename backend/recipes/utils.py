from uuid import uuid4


def generate_short_link():
    """Функция для генерации короткой ссылки."""
    return uuid4().hex[:6]
