from django.core.management.base import BaseCommand
from app001.models import Article, Commentary


class Command(BaseCommand):
    help = "Get all author's commentaries by article title"

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Article title')

    def handle(self, *args, **options):
        title = options.get('title')
        article = Article.objects.filter(title=title).first()
        commentaries = Commentary.objects.filter(article=article)
        if commentaries:
            self.stdout.write('\n'.join(
                [
                    f'Commentaries to article {article.title}:',
                    '\n'.join(map(str, commentaries))
                ]
            ))
        else:
            self.stdout.write("Not found")
    # Title 7
