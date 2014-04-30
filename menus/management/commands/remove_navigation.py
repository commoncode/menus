from django.core.management.base import BaseCommand

from ...models import Menu


class Command(BaseCommand):
    help = 'Clean up Footer'

    def handle(self, *args, **options):
        navigation = Menu.objects.get(name='Navigation')

        for item in navigation.items.all():
            item.link.delete()
            item.delete()

        navigation.delete()
