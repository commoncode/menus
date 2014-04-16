from django.core.management.base import BaseCommand

from ...models import Link, Menu, MenuItem


class Command(BaseCommand):
    help = 'Clean up Menus'

    def handle(self, *args, **options):
        Link.objects.all().delete()
        Menu.objects.all().delete()
        MenuItem.objects.all().delete()
