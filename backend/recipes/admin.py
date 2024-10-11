from django.contrib import admin
from django.contrib.admin import display

from .models import (Favorite, Ingredient, RecipeIngredients, Recipe,
                     ShoppingCart, Tag)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'added_in_favorites')
    readonly_fields = ('added_in_favorites',)
    list_filter = ('author', 'name', 'tags',)

    @display(description='Число добавлений в избранное рецепта')
    def added_in_favorites(self, obj):
        return obj.favorites.count()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)


@admin.register(Favorite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)


@admin.register(RecipeIngredients)
class IngredientInRecipe(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount',)
