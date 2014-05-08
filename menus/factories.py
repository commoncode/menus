import factory

from django.template.defaultfilters import slugify

from faker import Factory

from .fakers import words


fake = Factory.create()


class LinkFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'menus.Link'

    title = factory.LazyAttribute(lambda o: words(2).title())
    slug = factory.LazyAttribute(lambda o: slugify(words(3)))


class MenuFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'menus.Menu'
    FACTORY_DJANGO_GET_OR_CREATE = ('title', )

    title = factory.LazyAttribute(lambda o: words(2).title())
    slug = factory.LazyAttribute(lambda o: slugify(words(3)))


class MenuItemFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'menus.MenuItem'

    menu = factory.SubFactory(MenuFactory)
    link = factory.SubFactory(LinkFactory)
