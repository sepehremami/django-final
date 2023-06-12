from django.urls import path, include, re_path
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken import views as rest_views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"address", views.AddressViewSet, basename="address")
router.register(r"profile", views.ProfileViewSet, basename="profile")

urlpatterns = [
   
    path("login/", views.my_login, name="login"),
    # path("api/register/", views.RegisterUserAPIView.as_view(), name='register'),
    path(
        "api/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="refresh-token-obtain",
    ),
    path("api/token/verify/", jwt_views.TokenVerifyView.as_view(), name="token_verify"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("api/token/obtain/", view=views.ObtainTokenView.as_view(), name="otoken"),
    path("test/", view=views.index, name="otest"),
    path("api/", include(router.urls)),
    path('api/register/', views.RegisterViewSet.as_view(), name='register'),
    path("otp/", view=views.send_otp, name="otp"),
]
