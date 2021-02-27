from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from rest_framework.authtoken.models import Token


class LoginUserSerializer(serializers.ModelSerializer):
    """ Сериализатор для входа пользователя """

    email = serializers.EmailField(
                required=False, 
                validators=[UniqueValidator(queryset=User.objects.all())],
            )  
    password = serializers.CharField(min_length=8, required=True, 
                                     write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')


class RegisterUserSerializer(serializers.ModelSerializer):
    """ Сериализатор для регистрации пользователя с валидацией username, email и password """

    username = serializers.CharField(
                max_length=32,
                required=True,
                validators=[UniqueValidator(queryset=User.objects.all())],
            )
    email = serializers.EmailField(
                required=False, allow_blank=True,
                validators=[UniqueValidator(queryset=User.objects.all())],
            )
    password = serializers.CharField(min_length=8, required=True, 
                                     write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


class AuthUserSerializer(serializers.ModelSerializer):
    """ Сериализатор для подтверждения аутентификации пользователя с генерацией токена """

    token = serializers.SerializerMethodField('get_auth_token')

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 
                  'last_name', 'is_active', 'is_staff', 'token')
        read_only_fields = ('id', 'is_active', 'is_staff', 'token')

    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value


class EmptySerializer(serializers.Serializer):
    """ Сериализатор-заглушка, до выбора конкретного действия """
    pass

