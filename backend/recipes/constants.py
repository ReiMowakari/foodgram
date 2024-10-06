# Константы для приложения Recipe.

# Константа для длины поля модели Tag.
TAG_NAME_MAX_LENGTH: int = 32
# Константа для длины поля названия модели Ingredient.
INGREDIENT_NAME_MAX_LENGTH: int = 128
# Константа для длины поля единицы измерения модели Ingredient.
INGREDIENT_UNIT_MAX_LENGTH: int = 64
# Константа для длины поля названия модели Recipe.
RECIPE_NAME_MAX_LENGTH: int = 256
# Константа для минимального времени приготовления.
COOKING_TIME_MIN_VALUE: int = 1
# Константа для текста ошибки времени приготовления.
COOKING_TIME_ERROR_MESSAGE: str = (
    'Время приготовления не может быть меньше 1 минуты.'
)
# Константа для минимального кол-ва ингредиентов в рецепте.
AMOUNT_OF_INGREDIENT_MIN_VALUE: int = 1
# Константа для текста ошибки минимального кол-ва ингредиентов в рецепте.
AMOUT_OF_INGREDIENT_MIN_VALUE_ERROR_MESSAGE: str = (
    'Кол-во ингредиентов не может быть меньше 1.'
)