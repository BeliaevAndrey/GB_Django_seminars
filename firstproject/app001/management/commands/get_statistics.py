from django.core.management.base import BaseCommand
from app001.models import CoinPlay


class Command(BaseCommand):
    help = "Get stats on throws."

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Amount of last throws.')

    def handle(self, *args, **options):
        amount = options.get('amount')
        stat_dct = str(CoinPlay.get_throws(amount))
        self.stdout.write(stat_dct)
