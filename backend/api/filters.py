from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from rest_framework.filters import BaseFilterBackend

from recipes.models import Recipe

User = get_user_model()


class IngredientFilter(BaseFilterBackend):
    """Фильтр для Ингредиентов."""

    def filter_queryset(self, request, queryset, view):
        """Метод для поиска рецептов по указанному имени."""
        if 'name' in request.query_params:
            queryset = queryset.filter(
                name__startswith=request.query_params['name']
            )
        return queryset


class RecipeFilter(filters.FilterSet):
    """Фильтр для рецептов."""

    author = filters.ModelChoiceFilter(queryset=User.objects.all())
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    is_favorited = filters.BooleanFilter(
        field_name='is_favorited', method='filter_is_favorited')
    is_in_shopping_cart = filters.BooleanFilter(
        field_name='is_in_shopping_cart', method='filter_is_in_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = ('tags', 'author',)

    def filter_is_favorited(self, queryset, name, value):
        """Кастомный фильтр для избранного."""
        user = self.request.user
        if value is True and user.is_authenticated:
            return queryset.filter(is_favorited=user)
        if value is False and user.is_authenticated:
            return queryset.exclude(is_favorited=user)
        return queryset

    def filter_is_in_shopping_cart(self, queryset, name, value):
        """Кастомный фильтр для списка избранного."""
        user = self.request.user
        if value is True and user.is_authenticated:
            return queryset.filter(is_in_shopping_cart=user)
        return queryset
