from rest_framework import serializers
from access.models import User


class TokenCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField(allow_blank=False, trim_whitespace=True)


class PublicUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username",
            "bio",
            "avatar",
        ]
