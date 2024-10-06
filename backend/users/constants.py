# Константы для приложения User.

# Константа для максимальной длины поля ФИО для модели User.
FIO_MAX_FIELD_LENGTH: int = 150
# Константа для значения по-умолчанию лимита рецептов.
RECIPES_LIMIT: int = 10
# Константа ддя ошибки отсутствия аватара.
CHANGE_AVATAR_ERROR_MESSAGE: str = 'Изображение отсутствует.'
# Константа для ошибки, если подписка уже существует.
SUBSCRIBE_ERROR_MESSAGE: str = 'Вы уже подписаны на этого автора.'
# Константа для ошибки, если подписка уже существует.
SUBSCRIBE_SELF_ERROR_MESSAGE: str = 'Нельзя подписаться на самого себя.'
# Константа для ошибки удаления несуществующей подписки.
SUBSCRIBE_DELETE_ERROR_MESSAGE: str = 'Невозможно удалить несуществующую подписку.'
