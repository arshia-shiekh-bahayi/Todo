from django.urls import path, include
from ..views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("registration/", RegistrationApiView.as_view(), name="registration"),
    path(
        "activation/confirm/<str:token>", ActivationApiView.as_view(), name="activation"
    ),
    path(
        "activation/resend/",
        ActivationResendApiView.as_view(),
        name="activation-resend",
    ),
    path("change-password/", ChangePasswordApiView.as_view(), name="change-password"),
    path("token/login/", CustomObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", CustomDiscardAuthToken.as_view(), name="token-logout"),
    path("jwt/create/", CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]
