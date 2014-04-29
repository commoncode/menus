from random import choice, randint

from django.core.management.base import BaseCommand, CommandError

from commercia.products.models import Category

from ...factories import MenuFactory, MenuItemFactory


class Command(BaseCommand):
    help = 'Create a sample of menus'

    def handle(self, *args, **options):
        # Build Top Navigation
        navigation = MenuFactory(name='Navigation')
        categories = Category.objects.all().values_list('pk', flat=True)

        for i in range(randint(2, 4)):
            menu = MenuFactory(parent=navigation)

            print "Menu: {}".format(menu.name)

            for j in range(randint(1, 3)):
                submenu = MenuFactory(parent=menu)

                print "SubMenu: {}".format(submenu.name)

                for k in range(randint(2, 5)):
                    menuitem = MenuItemFactory(menu=submenu)
                    menuitem.link.object_id = choice(categories)
                    menuitem.link.save()

                    print "MenuItem: {}".format(menuitem.link.title)

                submenu.save()

            menu.save()

        navigation.save()

        # Build Footer Navigation
        print "Creating Footer"

        footer = MenuFactory(name='Footer')
        pages = ('Newsletter', 'About Us', 'Contact Us', 'Referral Program',
            'Store Locator', 'Help & FAQ\'s', 'Press', 'Sitemap',
            'Terms & Privacy', 'Blog')

        for page in pages:
            menuitem = MenuItemFactory(menu=footer)
            menuitem.link.title = page
            menuitem.link.save()

            print "Add Footer Item: {}".format(page)

        footer.save()
