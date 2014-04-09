from random import choice, randint

from django.core.management.base import BaseCommand, CommandError

from commercia.products.models import Category

from ...factories import MenuFactory, MenuItemFactory


class Command(BaseCommand):
    help = 'Create a sample of menus'

    def handle(self, *args, **options):
        categories = Category.objects.all().values_list('pk', flat=True)

        for i in range(randint(2, 4)):
            menu = MenuFactory()

            print "Menu: {}".format(menu.name)

            for j in range(randint(2, 5)):
                menuitem = MenuItemFactory(menu=menu)
                menuitem.link.object_id = choice(categories)
                menuitem.link.save()

                print "MenuItem: {}".format(menuitem.link.title)

            menu.save()
