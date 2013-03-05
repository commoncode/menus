from django.db import models
from entropy import base as entropy_base
from platforms.models import PlatformObjectManager

class Link(entropy_base.LinkURLMixin):
    '''
    Admin defined link for use in menus and about the site.
    '''

    # url
    # gfk
    absolute = models.BooleanField('Find for Store', default=False,
        help_text='Set to indicate we should try to find a store-relative URL for Objects',
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.url,)

    @staticmethod
    def autocomplete_search_fields():
        return ('title__icontains', 'slug__icontains',)

    def get_url(self, prefix):

        # Is a content type specified?
        if self.content_type:

            # Is there a specific object to look at?
            if self.object_id:
                try:
                    obj = self.content_object
                except AttributeError:
                    return '' # raise a validation error

                # should we try to find a StoreFOO?
                if self.absolute and hasattr(obj, 'get_store_url'):
                    return obj.get_store_url(prefix)
                return obj.get_absolute_url()

            else:
                try:
                    return self.content_type.model_class().get_store_list_url(prefix)
                except AttributeError:
                    return '' # raise a validation error

        # Fall back to url
        if self.url.startswith('http://') or \
            self.url.startswith('https://') or \
            self.url.startswith('/'):
            return self.url
        return '/%s/%s' % (prefix, self.url)


class Menu(entropy_base.EnabledMixin):
    '''An ordered collection of Links'''
    name = models.CharField(max_length=255)
    # enabled = base.EnabledField(default=True)

    def __unicode__(self):
        return self.name
        

class MenuInstance(models.Model):
    """
    Instantiate a Menu for a given Platform in a Template Position.
    """
    # platform = models.ForeignKey('platforms.Platform', null=True, blank=True,
    #     related_name='menus',
    #     help_text='Leave blank to set as default for this slug.',
    # )

    menu = models.ForeignKey('Menu')
    slug = models.SlugField(help_text='Name for this menu in templates')

    objects = PlatformObjectManager()

    def __unicode__(self):
        return u'%s' % (self.menu)


class MenuItem(models.Model):
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