import factory

from django.contrib.contenttypes.models import ContentType
from django.contrib.webdesign import lorem_ipsum
from django.template.defaultfilters import slugify

from faker import Factory



fake = Factory.create()


class LinkFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'menus.Link'

    title = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(2, common=False).title())
    slug = factory.LazyAttribute(
        lambda o: slugify(lorem_ipsum.words(3, common=False)))


class MenuFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'menus.Menu'

    name = factory.LazyAttribute(
        lambda o: lorem_ipsum.words(2, common=False).title())
    slug = factory.LazyAttribute(
        lambda o: slugify(lorem_ipsum.words(3, common=False).title()))


class MenuItemFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'menus.MenuItem'

    menu = factory.SubFactory(MenuFactory)
    link = factory.SubFactory(LinkFactory)
