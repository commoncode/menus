from django.db import models

from cqrs.models import CQRSModel
from entropy import base as entropy_base

try:
    # Only import from platforms if it is a dependancy
    from platforms import settings as platforms_settings
    if platforms_settings.USE_PLATFORMS:
        from platforms import models as platforms_models
        # Use platform mixin if platforms is found as a dependancy
        ObjectManager = platforms_models.PlatformObjectManager
    else:
        raise ImportError
except ImportError:
    ObjectManager = models.Manager


class Link(CQRSModel, entropy_base.LinkURLMixin):
    '''
    Admin defined link for use in menus and about the site.
    '''

    # url
    # gfk
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        if self.url:
            return u'%s (%s)' % (self.title, self.url,)
        else:
            return u'%s' % self.title

    @staticmethod
    def autocomplete_search_fields():
        return ('title__icontains', 'slug__icontains',)

    def get_url(self):

        # If a URL is specified, use that first
        if self.url:
            return self.url

        if self.content_type:

            if self.object_id:
                try:
                    obj = self.content_object
                except AttributeError:
                    return '' # raise a validation error

                if obj is None:
                    return ''

                return obj.get_absolute_url()
            else:
                try:
                    return self.content_type.model_class().get_list_url()
                except AttributeError:
                    return '' # raise a validation error

        return '' # raise a validation error


class Menu(CQRSModel, entropy_base.EnabledMixin):
    '''An ordered collection of Links'''
    name = models.CharField(max_length=255)
    slug = models.SlugField(help_text='Name for this menu in templates')
    objects = ObjectManager()

    def __unicode__(self):
        return self.name


class MenuItem(CQRSModel):
    menu = models.ForeignKey('Menu', related_name='items')
    link = models.ForeignKey('Link')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order',)

    def __unicode__(self):

        return u'%s :: %s' % (
            self.menu,
            self.link)

    def get_url(self, prefix):
        return self.link.get_url(prefix)

    def __getitem__(self, key):
        '''Allow dict access to Link attributes'''
        return getattr(self.link, key)
