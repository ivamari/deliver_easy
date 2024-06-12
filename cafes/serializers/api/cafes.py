from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from cafes.models.cafes import Cafe
from common.serializers.mixins import ExtendedModelSerializer
from users.serializers.nested.users import UserShortSerializer

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from crum import get_current_user

User = get_user_model()


class CafeSearchListSerializer(ExtendedModelSerializer):
    owner = UserShortSerializer(read_only=True)

    class Meta:
        model = Cafe
        fields = (
            'id',
            'name',
            'owner',
            'location',
        )


class CafeCreateSerializer(GeoFeatureModelSerializer):
    """Сериализатор для создания кафе"""
    owner = UserShortSerializer(read_only=True)

    class Meta:
        model = Cafe
        fields = ('id',
                  'name',
                  'owner',
                  'location',)
        geo_field = 'location'
        id_field = False

    def validate_name(self, value):
        if self.Meta.model.objects.filter(name=value):
            raise ParseError(
                'Кафе с таким названием уже существует.'
            )
        return value

    def validate_location(self, value):
        if self.Meta.model.objects.filter(location=value):
            raise ParseError(
                'Кафе с такой локацией уже существует.'
            )
        return value

    def validate(self, attrs):
        user = get_current_user()
        attrs['owner'] = user
        return attrs

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class CafeListSerializer(GeoFeatureModelSerializer):
    """Сериализатор для получения списка кафе"""
    owner = UserShortSerializer()
    pax = serializers.IntegerField()
    departments_count = serializers.IntegerField()
    can_manage = serializers.BooleanField()

    class Meta:
        model = Cafe
        geo_field = 'location'
        fields = ('id',
                  'name',
                  'owner',
                  'location',
                  'pax',
                  'departments_count',
                  'created_at',
                  'can_manage',)


class CafeRetrieveSerializer(GeoFeatureModelSerializer):
    """Сериализатор для получения данных о кафе"""
    owner = UserShortSerializer()
    pax = serializers.IntegerField()
    departments_count = serializers.IntegerField()
    can_manage = serializers.BooleanField()

    class Meta:
        model = Cafe
        geo_field = 'location'
        fields = ('id',
                  'name',
                  'owner',
                  'location',
                  'pax',
                  'departments_count',
                  'created_at',
                  'can_manage',
                  )


class CafeUpdateSerializer(GeoFeatureModelSerializer):
    """Сериализатор для частичного обновления данных о кафе"""

    class Meta:
        model = Cafe
        geo_field = 'location'
        fields = ('id',
                  'name',
                  'location',)
        id_field = False

    def validate_name(self, value):
        instance = self.instance
        if instance and instance.name == value:
            return value
        if Cafe.objects.filter(name=value).exists():
            raise ParseError("Кафе с таким именем уже существует.")
        return value

    def validate_location(self, value):
        instance = self.instance
        if instance and instance.location == value:
            return value
        if Cafe.objects.filter(location=value).exists():
            raise ParseError("Кафе с такой локацией уже существует.")
        return value
