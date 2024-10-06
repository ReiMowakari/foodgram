from django.urls import include, path
from rest_framework.routers import DefaultRouter

#from recipes.views import (
    #IngredientViewSet, RecipeViewSet, TagViewSet
#)
from users.views import UserViewSet
app_name = 'api'

api_v1 = DefaultRouter()

#router.register('ingredients', IngredientViewSet, basename='ingredient')
#router.register('recipes', RecipeViewSet, basename='recipe')
#router.register('tags', TagViewSet, basename='tag')
api_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(api_v1.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
