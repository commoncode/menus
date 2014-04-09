from cqrs.serializers import CQRSSerializer
from entropy.base import BaseLinkMixin, EnabledMixin, LinkURLMixin

from .models import Link, Menu, MenuItem


class BaseLinkMixinSerializer(CQRSSerializer):
    class Meta:
        model = BaseLinkMixin
        fields = (
            'id',
        )


class LinkURLMixinSerializer(CQRSSerializer):
    class Meta:
        model = LinkURLMixin
        fields = (
            'id',
        )


class EnabledMixinSerializer(CQRSSerializer):
    class Meta:
        model = EnabledMixin
        fields = (
            'id',
        )


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
