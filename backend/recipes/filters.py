from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from rest_framework.filters import BaseFilterBackend

from .models import Recipe

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

    class Meta:
        model = Recipe
        fields = ('tags', 'author',)
