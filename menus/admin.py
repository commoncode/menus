from django.contrib import admin
from menus import models

from platforms.admin import PlatformObjectInline

# class MenuItemInline(admin.TabularInline):
#     model = MenuItem
#     extra = 0
#     sortable_field_name = 'order'
#     raw_id_fields = ('link',)
#     autocomplete_lookup_fields = {
#         'fk': ('link',),
#     }
#     formfield_overrides = {
#         models.PositiveIntegerField: { 'widget': forms.HiddenInput }
#     }

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled',)
    list_filter = ('enabled',)

    inlines = (
        # MenuItemInline,
        # StoreMenuInline,
    )

admin.site.register(models.Menu, MenuAdmin)

class MenuInstanceAdmin(admin.ModelAdmin):
	list_display = ('menu', 'slug')
	inlines = [PlatformObjectInline,]

admin.site.register(models.MenuInstance, MenuInstanceAdmin)