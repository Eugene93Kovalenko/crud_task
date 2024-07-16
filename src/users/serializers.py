from typing import Dict, Any

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

    @staticmethod
    def validate_password(value: str) -> str:
        """
        Метод для валидации пароля, проверяет пароль с помощью стандартных валидаторов Django.
        """
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def create(self, validated_data: Dict[str, Any]) -> CustomUser:
        """
        Метод для создания нового пользователя, перед сохранением проверяет и хэширует пароль.
        """
        password = validated_data.pop('password')
        self.validate_password(password)

        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, user: CustomUser, validated_data: Dict[str, Any]) -> CustomUser:
        """
        Метод для обновления данных пользователя. Проверяет и хэширует новый пароль.
        """
        password = validated_data.pop('password', None)
        if password:
            self.validate_password(password)
            user.set_password(password)

        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        user.save()
        return user
