from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a sample of menus'

    def handle(self, *args, **options):
        call_command('create_navigation')
        call_command('create_footer')
