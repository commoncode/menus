from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Link, Menu
from .serializers import LinkSerializer, MenuSerializer


class LinkDocumentCollection(DRFDocumentCollection):
    model = Link
    serializer_class = LinkSerializer
    name = 'economica__links'


class MenuDocumentCollection(DRFDocumentCollection):
    model = Menu
    serializer_class = MenuSerializer
    name = 'economica__menus'


mongodb.register(LinkDocumentCollection())
mongodb.register(MenuDocumentCollection())
