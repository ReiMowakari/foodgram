import json
import os
from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загружает ингредиенты в БД из формата JSON'

    def handle(self, *args, **kwargs):
        file_path = os.path.join('data', 'ingredients.json')

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR('Файл не найден.'))
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for ingredient_data in data.get('ingredients', []):
            ingredient, created = Ingredient.objects.get_or_create(
                name=ingredient_data['name'],
                measurement_unit=ingredient_data['measurement_unit']
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Ингредиент "{ingredient.name}" создан'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Ингредиент "{ingredient.name}" уже существует.'
                    )
                )
        self.stdout.write(
            self.style.SUCCESS('Ингредиенты успешно загружены.'
                               )
        )
