from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User serializer class that provides create and update functionality"""
    # Set is_active field as required as in example
    # EXAMPLE: https://emphasoft-test-assignment.herokuapp.com/swagger/
    is_active = serializers.BooleanField(required=True)

    class Meta:
        # in case we use custom user model
        model = get_user_model()
        # fields list is same as in the example
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'is_active',
                  'last_login',
                  'is_superuser',
                  'password')
        read_only_fields = ('id', 'last_login', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        """
        update user instance and setting user password
        """
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def create(self, validated_data):
        """
        create user with password
        """
        return get_user_model().objects.create_user(**validated_data)
