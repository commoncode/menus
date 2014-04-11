import factory

from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify

from faker import Factory

from .fakers import words


fake = Factory.create()


class LinkFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'menus.Link'

    title = factory.LazyAttribute(lambda o: words(2).title())
    slug = factory.LazyAttribute(lambda o: slugify(words(3)))
    content_type = ContentType.objects.get(app_label='products',
        model='category')


class MenuFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'menus.Menu'

    name = factory.LazyAttribute(lambda o: words(2).title())
    slug = factory.LazyAttribute(lambda o: slugify(words(3)))


class MenuItemFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'menus.MenuItem'

    menu = factory.SubFactory(MenuFactory)
    link = factory.SubFactory(LinkFactory)
