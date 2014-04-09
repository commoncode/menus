from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Menu
from .serializers import MenuSerializer


class MenuDocumentCollection(DRFDocumentCollection):
    model = Menu
    serializer_class = MenuSerializer
    name = 'economica__menus'


mongodb.register(MenuDocumentCollection())
