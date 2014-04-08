from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Menu


class MenuDocumentCollection(DRFDocumentCollection):
    model = Menu
    name = 'economica__menus'


mongodb.register(MenuDocumentCollection())
