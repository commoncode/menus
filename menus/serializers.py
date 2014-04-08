from cqrs.serializers import CQRSSerializer

from .models import Link, Menu, MenuItem


class LinkSerializer(CQRSSerializer):
    class Meta:
        model = Link
        fields = (
            'id',
            'title',
            'url',
            'slug'
        )


class MenuItemSerializer(CQRSSerializer):
    link = LinkSerializer()

    class Meta:
        model = MenuItem
        fields = (
            'id',
            'menu',
            'order',
            'link'
        )


class MenuSerializer(CQRSSerializer):
    items = MenuItemSerializer(many=True)

    class Meta:
        model = Menu
        fields = (
            'id',
            'name',
            'items',
            'slug'
        )
