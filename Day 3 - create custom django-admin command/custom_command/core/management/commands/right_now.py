from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone


class Command(BaseCommand):
    help = "display current time"

    def add_arguments(self, parser):
        parser.add_argument('--times', nargs="+", type=int, help="how many time print time?")

    def handle(self, *args, **kwargs):
        times = kwargs['times']

        time = timezone.now().strftime('%X')
        self.stdout.write(f"It's : {time}")
