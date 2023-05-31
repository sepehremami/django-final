from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken import views as rest_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'address', views.AddressViewSet, basename='address')


urlpatterns = [
    # path("", views.ExampleView.as_view(), name='example'),
    path('login', views.UserLoginView.as_view(), name='login'),
    # path("api/register/", views.RegisterUserAPIView.as_view(), name='register'),
    path("api/token/", views.TokenObtainPairViewNew.as_view(), name="token-obtain"),
    path("api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="refresh-token-obtain"),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path('api/token/obtain/', view=views.ObtainTokenView.as_view(), name='otoken'),
    path('test/', view=views.index, name='otest'),
    path('api/', include(router.urls))  
]