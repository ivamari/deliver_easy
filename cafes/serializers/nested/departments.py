from rest_framework import serializers

from cafes.models.departments import Department


class DepartmentShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'name',
        )
