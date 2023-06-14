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
    # path("api/register/", views.RegisterUserAPIView.as_view(), name='register')
    path("api/", include(router.urls)),
    path('api/password/', view=views.ChangePasswordView.as_view(), name='change-password'),
    path("api/token/obtain/", view=views.ObtainTokenView.as_view(), name="otoken"),
    path('api/register/', views.RegisterViewSet.as_view(), name='register'),
    path("profile/<int:pk>/", views.ProfileView.as_view(), name="profile"),
    path("test/", view=views.index, name="otest"),
    path("otp/", view=views.send_otp, name="otp"),
    path("otp/validate/", view=views.validate_opt, name="validate-otp"),
    path("cart/<int:pk>/", view=views.CartTemplateView.as_view(), name="user-cart"),
    path("order/<int:pk>/", view=views.FinalOrderTemplateView.as_view(), name="user-order"),
]

