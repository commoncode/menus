from random import choice, randint

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError

from commercia.products.models import Category

from ...factories import LinkFactory, MenuFactory, MenuItemFactory


class Command(BaseCommand):
    help = 'Create the navigation'

    def handle(self, *args, **options):
        navigation = MenuFactory(name='Navigation')
        categories = Category.objects.all().values_list('pk', flat=True)

        for i in range(randint(2, 4)):
            menu = MenuFactory(parent=navigation)

            print "Menu: {}".format(menu.name)

            for j in range(randint(1, 3)):
                submenu = MenuFactory(parent=menu)

                print "SubMenu: {}".format(submenu.name)

                for k in range(randint(2, 5)):
                    c_type = ContentType.objects.get(app_label='products',
                        model='category')
                    link = LinkFactory(content_type=c_type,
                        object_id=choice(categories))
                    menuitem = MenuItemFactory(menu=submenu, link=link)

                    print "MenuItem: {}".format(menuitem.link.title)

                submenu.save()

            menu.save()

        navigation.save()
