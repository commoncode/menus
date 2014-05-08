from django.db import models

from cqrs.models import CQRSModel
from entropy.base import LinkURLMixin, TitleMixin, EnabledMixin, SlugMixin

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


class Link(CQRSModel, LinkURLMixin):
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
        return ('title__icontains', 'slug__icontains', )

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


<<<<<<< HEAD
class MenuInstance(CQRSModel):
    '''
    An instantiation of a Menu on a given Platform and Position

    Menu's display in their given Position across all Links.
    '''
    platforms = models.ManyToManyField(
        'platforms.Platform')
    position = models.ForeignKey(
        'positions.Position')


class Menu(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    '''An ordered collection of Links'''

=======
class Menu(CQRSModel, TitleMixin, EnabledMixin, SlugMixin):
    '''An ordered collection of Links'''
>>>>>>> 042555dcd6c8bba6c91485d90a0e70c977494fa7
    objects = ObjectManager()

    def __unicode__(self):
        return self.title


class MenuItem(CQRSModel):
    menu = models.ForeignKey('Menu', related_name='items')
    link = models.ForeignKey('Link')
    order = models.PositiveIntegerField(default=0)
    parent = models.ForeignKey('self', null=True, related_name='children')

    class Meta:
        ordering = ('order', )

    def __unicode__(self):

        return u'%s :: %s' % (
            self.menu,
            self.link)

    def get_url(self, prefix):
        return self.link.get_url(prefix)

    def __getitem__(self, key):
        '''Allow dict access to Link attributes'''
        return getattr(self.link, key)
