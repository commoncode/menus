from django import template
from menus.models import Menu

register = template.Library()

@register.inclusion_tag('menus/menu_list.html', takes_context=True)
def render_menu(context, *args, **kwargs):
    request = context['view'].request

    if getattr(Menu.objects, "platform"):
        # TODO: More than one menu...?
        query = Menu.objects.platform(request.platform).get()
    else:
        # TODO: More than one menu...?
        query = Menu.objects.get()
    # import ipdb; ipdb.set_trace()
    context["menu"] = query
    context["current_path"] = request.path
    return context