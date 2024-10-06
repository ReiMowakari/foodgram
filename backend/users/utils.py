import base64
from django.core.files.base import ContentFile
from rest_framework import serializers

from .models import Subscription


def get_follow_object(follower, following):
    """
    Получение связи объекта текущего пользователя и указанного.
    :param follower: передаётся объект текущего пользователя.
    :param following: передаётся объект указанного пользователя.
    :return: Возвращает объект подписки.
    """
    return Subscription.objects.get(user=follower, following=following)


def get_is_subscribed(self, obj):
    """
    Функция для проверки подписан ли текущий пользователь на указанного.
    :param self: передаётся объект текущего пользователя.
    :param obj: передаётся объект указанного пользователя
    :return: Возвращает булевое значение, в зависимости есть ли подписка или нет.
    """
    user = self.context['request'].user
    # Проверка на авторизацию текущего пользователя.
    if not user.is_authenticated:
        return False
    # Получение связи объекта текущего пользователя и указанного.
    follow = get_follow_object(user, obj)
    if follow.exists():
        return True
    return False


class Base64ImageField(serializers.ImageField):
    """Кастомный класс для расширения стандартного ImageField."""

    def to_internal_value(self, data):
        """Метод для формата base64"""
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)
