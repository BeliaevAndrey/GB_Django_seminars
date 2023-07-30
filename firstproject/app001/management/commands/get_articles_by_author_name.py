from django.core.management.base import BaseCommand
from app001.models import Article, Author


class Command(BaseCommand):
    help = "Get all author's articles by author surname and name"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Author name')
        parser.add_argument('surname', type=str, help='Author surname')

    def handle(self, *args, **options):
        surname = options.get('surname')
        name = options.get('name')
        author = Author.objects.filter(surname=surname, name=name).first()
        if author:
            articles = Article.objects.filter(author=author)
            self.stdout.write('\n'.join(
                [
                    f'Articles by {author.get_fullname()}:',
                    '\n'.join(map(str, articles)),
                ]
            ))
        else:
            self.stdout.write("Not found")
        # Author Nm2 Author Snm2
