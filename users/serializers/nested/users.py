from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'full_name',
        )


class UserEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'full_name',
            'email',
            'phone_number',
            'is_work_account',
        )
