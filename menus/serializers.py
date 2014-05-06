from rest_framework import serializers

from cqrs.serializers import CQRSSerializer

from .models import Link, Menu, MenuItem


class LinkSerializer(CQRSSerializer):
    object_id = serializers.IntegerField(source='object_id', read_only=True)

    class Meta:
        model = Link
        fields = (
            'id',
            'object_id',
            'title',
            'slug'
        )


class MenuItemSerializer(CQRSSerializer):
    link = LinkSerializer()

    class Meta:
        model = MenuItem
        fields = (
            'order',
            'link'
        )


class MenuSerializer(CQRSSerializer):
    items = MenuItemSerializer(many=True)

    class Meta:
        model = Menu
        fields = (
            'title',
            'collection',
            'items',
            'parent',
            'slug'
        )
