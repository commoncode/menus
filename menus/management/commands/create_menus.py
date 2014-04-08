from django.core.management.base import BaseCommand, CommandError

from ... import factories


class Command(BaseCommand):
    help = 'Create a sample of menus'

    def handle(self, *args, **options):
        for i in range(3):
            menu = factories.MenuFactory()

            print "Menu: {}".format(menu.name)

            for j in range(10):
                menuitem = factories.MenuItemFactory(menu=menu)

                print "MenuItem: {}".format(menuitem.link.title)
