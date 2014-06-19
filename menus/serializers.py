import json

from django.core import serializers as django_serializers
from rest_framework import serializers

from cqrs.serializers import CQRSSerializer
from images.serializers import ImageInstanceSerializer

from .models import Link, Menu, MenuItem


class LinkSerializer(CQRSSerializer):

    content_type = serializers.CharField(
        source='get_content_type',
        read_only=True)

    object_id = serializers.IntegerField(
        source='object_id',
        read_only=True)

    content_object = serializers.SerializerMethodField('get_content_object')

    class Meta:
        model = Link

    def get_content_object(self, obj):

        if obj.content_object:
            data = django_serializers.serialize('json', [obj.content_object,])
            return json.loads(data)[0]['fields']

        return obj.content_object


class MenuItemSerializer(CQRSSerializer):

    link = LinkSerializer()
    image = ImageInstanceSerializer()

    class Meta:
        model = MenuItem


class MenuSerializer(CQRSSerializer):

    items = MenuItemSerializer(many=True)

    class Meta:
        model = Menu
