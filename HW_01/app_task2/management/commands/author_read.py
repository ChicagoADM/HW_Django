from django.core.management.base import BaseCommand

from app_task2.models import Author


class Command(BaseCommand):
    help = "Get author by id"

    def add_arguments(self, parser):
        parser.add_argument('author_id', type=str, help='Author id')

    def handle(self, *args, **kwargs):
        author_id = kwargs.get('author_id')
        author = Author.objects.filter(id=author_id).first()
        self.stdout.write(f'{author}')