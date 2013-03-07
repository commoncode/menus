from django import template
from menus.models import Menu

register = template.Library()

@register.inclusion_tag('menus/menu_list.html', takes_context=True)
def render_menu(context, slug, *args, **kwargs):
    request = context['view'].request

    try:
        if getattr(Menu.objects, "platform", False):
            query = Menu.objects.platform(request.platform).get(
                enabled=True,
                slug=slug
                )
        else:
            query = Menu.objects.get(
                enabled=True,
                slug=slug
                )
    except Menu.DoesNotExist, Menu.MultipleObjectsReturned:
        query = None

    context["menu"] = query
    context["current_path"] = request.path
    return context