from random import choice

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError

from pages.models import Page

from ...factories import LinkFactory, MenuFactory, MenuItemFactory


class Command(BaseCommand):
    help = 'Create the footer'

    def handle(self, *args, **options):
        print "Creating Footer"

        footer = MenuFactory(name='Footer')
        titles = ('Newsletter', 'About Us', 'Contact Us', 'Referral Program',
            'Store Locator', 'Help & FAQ\'s', 'Press', 'Sitemap',
            'Terms & Privacy', 'Blog')
        pages = Page.objects.all().values_list('pk', flat=True)

        for title in titles:
            c_type = ContentType.objects.get(app_label='pages', model='page')
            link = LinkFactory(content_type=c_type, title=title,
                object_id=choice(pages))
            menuitem = MenuItemFactory(menu=footer, link=link)

            print "Add Footer Item: {}".format(title)

        footer.save()
