from django.contrib import admin
from menus import models as menu_models
from django import forms
from django.db import models

try:
    # Only import from platforms if it is a dependancy
    from platforms import settings as platforms_settings
    if platforms_settings.USE_PLATFORMS:
        from platforms import admin as platforms_admin
        # Use platform mixin if platforms is found as a dependancy
        PlatformObjectInline = [platforms_admin.PlatformObjectInline]
    else:
        raise ImportError
except ImportError:
    PlatformObjectInline = []


class LinkAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'slug',
        'url',)

    list_edit = (
        'title',
        'slug',
        'url',)

    list_filter = ('content_type',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug',),
        }),
        ('Object', {
            'fields': ('content_type', 'object_id',),
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

    inlines = [
        MenuItemInline
    ] + PlatformObjectInline

admin.site.register(menu_models.Menu, MenuAdmin)
