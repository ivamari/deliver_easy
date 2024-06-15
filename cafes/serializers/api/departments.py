from django.contrib.auth import get_user_model
from rest_framework import serializers

from cafes.models.cafe_departments import CafeDepartment
from cafes.models.cafes import Cafe
from cafes.models.departments import Department
from common.serializers.mixins import ExtendedModelSerializer
from users.serializers.nested.users import (UserShortSerializer,)

User = get_user_model()


########################
# DEPARTMENTS
########################

class DepartmentLittleListSerializer(ExtendedModelSerializer):
    """Сериализатор для списка отделов"""

    class Meta:
        model = Department
        fields = (
            'id',
            'name',
        )


#################################
# CAFE_DEPARTMENTS_LIST_RETRIEVE
#################################

class DepartmentCafeListRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для кафе/отделов. Используется в GET-запросах к кафе"""
    id = serializers.IntegerField(source='department.id')
    name = serializers.CharField(source='department.name')
    manager = UserShortSerializer()
    members = UserShortSerializer(read_only=True, many=True,
                                  source='members_set.all')

    class Meta:
        model = CafeDepartment
        fields = (
            'id',
            'name',
            'manager',
            'members',
        )


class CafeDepartmentListSerializer(ExtendedModelSerializer):
    """Сериализатор для списка кафе с отделами"""
    owner = UserShortSerializer()
    departments = DepartmentCafeListRetrieveSerializer(many=True,
                                                       source='cafe_departments')

    class Meta:
        model = Cafe
        fields = (
            'id',
            'name',
            'owner',
            'location',
            'departments',
        )
        read_only_fields = fields


class CafeDepartmentRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для получения кафе с отделами"""
    owner = UserShortSerializer()
    departments = DepartmentCafeListRetrieveSerializer(many=True,
                                                       source='cafe_departments')

    class Meta:
        model = Cafe
        fields = (
            'id',
            'name',
            'owner',
            'location',
            'departments',
        )
        read_only_fields = fields


########################
# CAFE_DEPARTMENTS_UPDATE
########################

class DepartmentCafeRepresentationSerializer(ExtendedModelSerializer):
    """Сериализатор для кафе/отделов. Используется в to_representation"""
    id = serializers.IntegerField(source='department.id')
    name = serializers.CharField(source='department.name')
    manager = UserShortSerializer()
    members = UserShortSerializer()

    class Meta:
        model = CafeDepartment
        fields = (
            'id',
            'name',
            'manager',
            'members',
        )


class CafeDepartmentRepresentationSerializer(ExtendedModelSerializer):
    """Сериализатор для получения кафе с отделами"""
    owner = UserShortSerializer()
    departments = DepartmentCafeRepresentationSerializer(many=True,
                                                         source='cafe_departments')

    class Meta:
        model = Cafe
        fields = (
            'id',
            'name',
            'owner',
            'location',
            'departments',
        )
        read_only_fields = fields


class DepartmentCafeCreateUpdateSerializer(ExtendedModelSerializer):
    """Сериализатор для кафе/отделов.
    Используется при добавлении отделов в кафе"""
    id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),
                                            source='cafe_departments'
                                            )
    manager = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='departments_manager',
    )
    members = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='departments_members',
    )

    class Meta:
        model = CafeDepartment
        fields = (
            'id',
            'manager',
            'members',
        )


class CafeDepartmentCreateUpdateSerializer(ExtendedModelSerializer):
    """Сериализатор для добавления отделов в кафе"""
    departments = DepartmentCafeCreateUpdateSerializer(many=True)

    class Meta:
        model = Cafe
        fields = (
            'id',
            'name',
            'owner',
            'location',
            'departments',
        )
        read_only_fields = ('name', 'owner', 'location')

    def create_cafe_departments(self, cafe, departments_cafe):
        cafe_departments = []
        for department in departments_cafe:
            cafe_departments.append(
                CafeDepartment(cafe=cafe,
                               department=department['cafe_departments'],
                               manager=department['departments_manager'],
                               members=department['departments_members'],
                               ))
        CafeDepartment.objects.bulk_create(cafe_departments)

    def update(self, cafe, validated_data):
        departments_data = validated_data.pop('departments')
        super().update(cafe, validated_data)
        CafeDepartment.objects.filter(cafe=cafe).delete()
        self.create_cafe_departments(cafe, departments_data)
        cafe.save()
        return cafe

    def to_representation(self, instance):
        request = self.context.get('request')
        return CafeDepartmentRepresentationSerializer(instance,
                                                      context={
                                                          'request': request}).data
