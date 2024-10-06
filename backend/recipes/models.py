from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from .constants import (
    TAG_NAME_MAX_LENGTH, INGREDIENT_NAME_MAX_LENGTH,
    INGREDIENT_UNIT_MAX_LENGTH, RECIPE_NAME_MAX_LENGTH,
    AMOUNT_OF_INGREDIENT_MIN_VALUE, AMOUT_OF_INGREDIENT_MIN_VALUE_ERROR_MESSAGE
)
from .validators import validate_cooking_time


User = get_user_model()


class Tag(models.Model):
    """Модель для тегов."""

    name = models.CharField(
        max_length=TAG_NAME_MAX_LENGTH,
        verbose_name='Название',
    )
    slug = models.SlugField(
        verbose_name='Уникальный слаг',
        max_length=TAG_NAME_MAX_LENGTH
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель для ингредиентов."""

    name = models.CharField(max_length=INGREDIENT_NAME_MAX_LENGTH,
                            verbose_name='Название')
    measurement_unit = models.CharField(
        max_length=INGREDIENT_UNIT_MAX_LENGTH,
        verbose_name='Единица измерения веса'
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        default_related_name = 'ingredient'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель для рецептов."""

    name = models.CharField(max_length=RECIPE_NAME_MAX_LENGTH,
                            verbose_name='Название')
    text = models.TextField('Описание')
    cooking_time = models.PositiveSmallIntegerField(
        validators=[validate_cooking_time],
        verbose_name='Время приготовления(в минутах)',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор рецепта',
        related_name='recipes'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Список ингредиентов'
    )
    image = models.ImageField(
        upload_to='recipes/images/',
        null=True,
        default=None,
        verbose_name='Аватар рецепта.'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        default_related_name = 'recipe'
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date', 'name')
        default_permissions = (
            'add', 'change', 'delete', 'view'
        )

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    """Промежуточная модель для связи рецептов и ингредиентов."""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        null=True,
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        null=True,
    )
    amount = models.SmallIntegerField(
        verbose_name='Количество',
        validators=[
            MinValueValidator(
                AMOUNT_OF_INGREDIENT_MIN_VALUE,
                AMOUT_OF_INGREDIENT_MIN_VALUE_ERROR_MESSAGE
            )
        ],
    )

    class Meta:
        default_related_name = 'recipe_ingredient'

    def __str__(self):
        return f'{self.amount}'


class RecipeTag(models.Model):
    """Промежуточная модель для связи рецептов и тэгов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Пользователь'
    )

    recipe = models.ForeignKey(Recipe,
                               on_delete=models.SET_NULL,
                               null=True,
    )
    tag = models.ForeignKey(Tag,
                            on_delete=models.SET_NULL,
                            null=True,
    )

    class Meta:
        default_related_name = 'recipe_tags'
        abstract = True

    def __str__(self):
        return f'{self.recipe} {self.tag}'


class ShoppingCart(models.Model):
    """Модель для списка покупок."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Рецепт'
    )

    class Meta:
        default_related_name = 'shopping_recipe'
        abstract = True


class FavoriteList(models.Model):
    """Модель для списка избранных рецептов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Рецепт'
    )

    class Meta:
        default_related_name = 'favorite_recipe'
        abstract = True
