from random import choice, randint

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError

from commercia.products.models import Category, Collection

from ...factories import LinkFactory, MenuFactory, MenuItemFactory


class Command(BaseCommand):
    help = 'Create the navigation'

    def handle(self, *args, **options):
        navigation = MenuFactory(title='Navigation')
        collections = list(Collection.objects.all())
        c_type = ContentType.objects.get(app_label='products',
            model='category')

        for i in range(randint(2, 4)):
            if not collections:
                break

            menu = MenuFactory(parent=navigation)

            print "Menu: {}".format(menu.title)

            for j in range(randint(2, 4)):
                if not collections:
                    break

                collection = collections.pop()
                submenu = MenuFactory(parent=menu, title=collection.title)
                collection.menu = submenu
                collection.save()

                print "SubMenu: {}".format(submenu.title)

                for category in collection.categories.all():
                    link = LinkFactory(content_type=c_type,
                        object_id=category.pk)
                    menuitem = MenuItemFactory(menu=submenu, link=link)

                    print "MenuItem: {}".format(menuitem.link.title)

                submenu.save()

            menu.save()

        navigation.save()
