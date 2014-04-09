from random import randint

from django.core.management.base import BaseCommand, CommandError

from ... import factories


class Command(BaseCommand):
    help = 'Create a sample of menus'

    def handle(self, *args, **options):
        for i in range(randint(0, 3)):
            menu = factories.MenuFactory()

            print "Menu: {}".format(menu.name)

            for j in range(randint(0, 10)):
                menuitem = factories.MenuItemFactory(menu=menu)

                print "MenuItem: {}".format(menuitem.link.title)
