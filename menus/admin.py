from django.contrib import admin
from menus import models as menu_models
from django import forms
from django.db import models

try:
    # Only import from platforms if it is a dependancy
    from platforms import admin as platforms_admin
    # Use platform mixin if platforms is found as a dependancy
    PlatformInlineMixin = platforms_admin.PlatformInlineMixin
except ImportError:
    PlatformInlineMixin = object
   

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


class MenuAdmin(PlatformInlineMixin, admin.ModelAdmin):
    list_display = ('name', 'enabled',)
    list_filter = ('enabled',)

    inlines = [MenuItemInline,]

admin.site.register(menu_models.Menu, MenuAdmin)
