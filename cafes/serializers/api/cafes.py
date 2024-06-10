from django.contrib.auth import get_user_model
from rest_framework.exceptions import ParseError

from cafes.models.cafes import Cafe
from users.serializers.nested.users import UserShortSerializer

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from crum import get_current_user

User = get_user_model()


class CafeCreateSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Cafe
        fields = ('id',
                  'name',
                  'location',)
        geo_field = 'location'
        id_field = False

    def validate_name(self, value):
        if self.Meta.model.objects.filter(name=value):
            raise ParseError(
                'Организация с таким названием уже существует'
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
    owner = UserShortSerializer()

    class Meta:
        model = Cafe
        geo_field = 'location'
        fields = ('id',
                  'name',
                  'owner',
                  'location',)


class CafeRetrieveSerializer(GeoFeatureModelSerializer):
    owner = UserShortSerializer()

    class Meta:
        model = Cafe
        geo_field = 'location'
        fields = ('id',
                  'name',
                  'owner',
                  'location',)


class CafeUpdateSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Cafe
        geo_field = 'location'
        fields = ('id',
                  'name',
                  'location',)
        id_field = False
