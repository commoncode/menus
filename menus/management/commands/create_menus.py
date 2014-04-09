from random import randint

from django.core.management.base import BaseCommand, CommandError

from commercia.products.factories import CategoryFactory, ProductFactory

from ...factories import MenuFactory, MenuItemFactory


class Command(BaseCommand):
    help = 'Create a sample of menus'

    def handle(self, *args, **options):
        for i in range(randint(2, 4)):
            menu = MenuFactory()

            print "Menu: {}".format(menu.name)

            for j in range(randint(2, 5)):
                menuitem = MenuItemFactory(menu=menu)

                print "MenuItem: {}".format(menuitem.link.title)

            menu.save()
