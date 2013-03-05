from django.contrib import admin
from menus import models as menu_models
from django import forms
from django.db import models

try:
    # Only import from platforms if it is a dependancy
    from platforms.admin import PlatformObjectInline
    from platforms import settings as platforms_settings
except ImportError:
    pass

class LinkAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'slug',
        'absolute',
        'url',)

    list_edit = (
        'title',
        'slug',
        'absolute',
        'url',)

    list_filter = ('absolute',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug',),
        }),
        ('Object', {
            'fields': ('content_type', 'object_id', 'absolute',),
        }),
        ('Raw URL', {
            'fields': ('url',),
        }),
    )

    autocomplete_lookup_fields = {
        'generic': [
            ['content_type', 'object_id'],],
    }

    prepopulated_fields = {
        'slug': ('title',),
    }

admin.site.register(menu_models.Link, LinkAdmin)


class MenuItemInline(admin.TabularInline):
    model = menu_models.MenuItem
    extra = 0
    sortable_field_name = 'order'
    raw_id_fields = ('link',)
    autocomplete_lookup_fields = {
        'fk': ('link',),
    }
    formfield_overrides = {
        models.PositiveIntegerField: { 'widget': forms.HiddenInput }
    }


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled',)
    list_filter = ('enabled',)

    inlines = (
        MenuItemInline,
    )

admin.site.register(menu_models.Menu, MenuAdmin)


class MenuInstanceAdmin(admin.ModelAdmin):
    list_display = ('menu', 'slug')

    def __init__(self, model, admin_site):
        # Check to see if platforms is installed, and if it is,
        # whether or not to use it in the admin
        try:
            if platforms_settings.USE_PLATFORMS:
                self.__class__.inlines = [PlatformObjectInline,]
        except NameError:
            pass 
        super(MenuInstanceAdmin, self).__init__(model, admin_site)


admin.site.register(menu_models.MenuInstance, MenuInstanceAdmin)