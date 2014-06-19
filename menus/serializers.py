from rest_framework import serializers

from cqrs.serializers import CQRSSerializer

from .models import Link, Menu, MenuItem


class LinkSerializer(CQRSSerializer):

    content_type = serializers.CharField(
        source='get_content_type',
        read_only=True)

    object_id = serializers.IntegerField(
        source='object_id',
        read_only=True)

    class Meta:
        model = Link


class MenuItemSerializer(CQRSSerializer):
    link = LinkSerializer()

    class Meta:
        model = MenuItem
        exclude = 'menu',


class MenuSerializer(CQRSSerializer):
    items = MenuItemSerializer(many=True)

    class Meta:
        model = Menu
        fields = (
            'title',
            'items',
            'slug'
        )
