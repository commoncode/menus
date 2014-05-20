from random import choice, randint

from django.contrib.contenttypes.models import ContentType
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from commercia.products.models import Category

from ...factories import LinkFactory, MenuFactory, MenuItemFactory


class Command(BaseCommand):
    help = 'Create the navigation'

    def handle(self, *args, **options):
        menu = MenuFactory(title='Navigation')
        c_type = ContentType.objects.get(app_label='products',
            model='category')
        categories = Category.objects.filter(parent__isnull=True)

        if not categories.exists():
            call_command('create_categories')

        categories = list(categories)

        while categories:
            item = MenuItemFactory(menu=menu)
            print "MenuItem: {}".format(item)

            for j in range(randint(2, 4)):
                if not categories:
                    break

                category = categories.pop()
                link = LinkFactory(content_type=c_type, object_id=category.pk,
                    title=category.title, slug=category.slug)
                subitem = MenuItemFactory(menu=menu, parent=item, link=link)

                print ">> {}".format(subitem)

                for subcategory in category.children.all():
                    sublink = LinkFactory(content_type=c_type,
                        object_id=subcategory.pk, title=subcategory.title,
                        slug=subcategory.slug)
                    subsubitem = MenuItemFactory(menu=menu, link=sublink,
                        parent=subitem)

                    print ">>>> {}".format(subsubitem)

        menu.save()
