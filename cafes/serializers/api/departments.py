from django.contrib.auth import get_user_model
from rest_framework import serializers

from cafes.models.cafe_departments import CafeDepartment
from cafes.models.cafes import Cafe
from cafes.models.departments import Department

from common.serializers.mixins import ExtendedModelSerializer
from users.serializers.nested.users import UserShortSerializer


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


###################################
# CAFE_DEPARTMENTS_LIST_RETRIEVE
###################################

class DepartmentCafeListRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для кафе/отделов. Используется в GET-запросах к кафе"""
    id = serializers.IntegerField(source='department.id')
    name = serializers.CharField(source='department.name')
    manager = UserShortSerializer()
    members = UserShortSerializer(read_only=True, many=True)

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
                                                       source='cafe_departments'
                                                       )
    pax = serializers.IntegerField()
    departments_count = serializers.IntegerField()
    can_manage = serializers.BooleanField()

    class Meta:
        model = Cafe
        fields = (
            'id',
            'name',
            'owner',
            'location',
            'departments',
            'pax',
            'departments_count',
            'can_manage',
        )
        read_only_fields = fields


class CafeDepartmentRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для получения кафе с отделами"""
    owner = UserShortSerializer()
    departments = DepartmentCafeListRetrieveSerializer(many=True,
                                                       source='cafe_departments')
    pax = serializers.IntegerField()
    departments_count = serializers.IntegerField()
    can_manage = serializers.BooleanField()

    class Meta:
        model = Cafe
        fields = (
            'id',
            'name',
            'owner',
            'location',
            'departments',
            'pax',
            'departments_count',
            'can_manage',
        )
        read_only_fields = fields


##########################
# CAFE_DEPARTMENTS_ADD
##########################

class DepartmentCafeRepresentationSerializer(ExtendedModelSerializer):
    """Сериализатор для кафе/отделов. Используется в to_representation"""
    id = serializers.IntegerField(source='department.id')
    name = serializers.CharField(source='department.name')
    manager = UserShortSerializer()
    members = UserShortSerializer(many=True)

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
                                            source='cafe_departments')
    manager = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='departments_manager',
    )
    members = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='departments_members',
        many=True
    )

    class Meta:
        model = CafeDepartment
        fields = (
            'id',
            'manager',
            'members',
        )

    def validate(self, data):
        manager = data.get('departments_manager')
        cafe = data.get('cafe_departments')

        if Cafe.objects.filter(pk=cafe.id, owner=manager).exists():
            raise serializers.ValidationError(
                'Владелец кафе не может быть менеджером.')

        cafe_department = self.instance
        members = data.get('departments_members')

        for member in members:
            if cafe_department:
                other_departments = CafeDepartment.objects.exclude(
                    id=cafe_department.id).filter(member=member)
            else:
                other_departments = CafeDepartment.objects.filter(
                    members=member)

            if other_departments.exists():
                raise serializers.ValidationError(
                    f'Сотрудник {member} уже состоит в другом отделе.'
                )

        return data


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
            cafe_department = CafeDepartment(
                cafe=cafe,
                department=department['cafe_departments'],
                manager=department['departments_manager']
            )
            cafe_departments.append(cafe_department)

        CafeDepartment.objects.bulk_create(cafe_departments)

        for cafe_department, department in zip(cafe_departments,
                                               departments_cafe):
            cafe_department.members.set(department['departments_members'])

    def update(self, cafe, validated_data):
        departments_data = validated_data.pop('departments')
        super().update(cafe, validated_data)
        self.create_cafe_departments(cafe, departments_data)
        cafe.save()
        return cafe

    def to_representation(self, instance):
        request = self.context.get('request')
        return CafeDepartmentRepresentationSerializer(
            instance, context={'request': request}).data
