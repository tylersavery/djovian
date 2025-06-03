from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.settings import api_settings as jwt_settings

from access.api.serializers import TokenCreateSerializer, TokenRefreshSerializer
from api import exceptions
from api.permissions import AllowAny
from access.models import User


class TokenCreateView(jwt_views.TokenViewBase):
    permission_classes = [AllowAny]
    serializer_class = TokenCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")

        user = authenticate(request=request, email=email, password=password)

        if not user:
            raise exceptions.AuthenticationFailed()

        try:
            refresh = RefreshToken.for_user(user)
        except TokenError:
            raise exceptions.BadRequest()

        return Response(
            {"access": str(refresh.access_token), "refresh": str(refresh)},
            status=status.HTTP_200_OK,
        )


class TokenRefreshView(jwt_views.TokenViewBase):
    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            refresh = RefreshToken(serializer.validated_data.get("refresh"))
        except TokenError:
            raise exceptions.BadRequest()

        if jwt_settings.ROTATE_REFRESH_TOKENS:
            refresh.set_jti()
            refresh.set_exp()

        return Response(
            {"access": str(refresh.access_token), "refresh": str(refresh)},
            status.HTTP_200_OK,
        )
