from django.core.exceptions import ValidationError

from .constants import COOKING_TIME_MIN_VALUE, COOKING_TIME_ERROR_MESSAGE


def validate_cooking_time(value):
    """Валидатор для проверки минимального времени приготовления."""
    if value < COOKING_TIME_MIN_VALUE:
        raise ValidationError(message=COOKING_TIME_ERROR_MESSAGE)
