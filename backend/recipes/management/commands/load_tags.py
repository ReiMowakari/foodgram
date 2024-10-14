import json
import os
from django.core.management.base import BaseCommand
from recipes.models import Tag


class Command(BaseCommand):
    help = 'Загружает тэги в БД из формата JSON'

    def handle(self, *args, **kwargs):
        file_path = os.path.join('data', 'tags.json')

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR('Файл не найден.'))
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for tags_data in data.get('tags', []):
            tag, created = Tag.objects.get_or_create(
                name=tags_data['name'],
                slug=tags_data['slug']
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Тэг "{tag.name}" создан'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Тэг "{tag.name}" уже существует.'
                    )
                )
        self.stdout.write(
            self.style.SUCCESS('Тэги успешно загружены.'
            )
        )
