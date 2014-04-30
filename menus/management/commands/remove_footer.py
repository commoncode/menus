from django.core.management.base import BaseCommand

from ...models import Menu


class Command(BaseCommand):
    help = 'Clean up Footer'

    def handle(self, *args, **options):
        footer = Menu.objects.filter(name='Footer')

        for item in footer.items.all():
            item.link.delete()
            item.delete()

        footer.delete()
