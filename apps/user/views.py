from django.contrib.auth.views import LoginView
from django.shortcuts import render
from apps.cart.models import OrderInfo
from apps.user.backends import JWTAuthBackend
from apps.user.models import User, Address
from django.contrib.auth.views import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from apps.user.tasks import send_otp_code
from .serializers import ObtainTokenSerializer, UserRegisterSerializer, UserSerializer, AddressSerializer, OTPCodeSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions, views as api_views
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes, api_view
from rest_framework.authtoken.views import ObtainAuthToken
from django.core.cache import cache
from rest_framework import status
from django.shortcuts import redirect
from django.urls import reverse


User = get_user_model()

from django.contrib.auth.middleware import AuthenticationMiddleware

class AuthenticationRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        auth_cookie = request.COOKIES.get('access')
        if auth_cookie is None:
            return redirect(reverse('landing'))
        return super().dispatch(request, *args, **kwargs)
        


class ProfileView(AuthenticationRequiredMixin, TemplateView):
    model = User
    template_name = "user/profile.html"


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        if isinstance(user, User):
            addresses = Address.objects.filter(user=user)
            context['addresses'] = addresses
            orders = OrderInfo.objects.filter(user=user)
            context['orders'] =orders      
        return context




# TODO: write otp authentication back
class ObtainTokenView(ObtainAuthToken):
    permission_classes = [permissions.AllowAny]
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer: ObtainTokenSerializer = self.serializer_class(data=request.data,  context={'request': request})
        serializer.is_valid(raise_exception=True)
        # alg_otp_code = serializer.validated_data.get('otp_code')
        username_or_phone = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        print(username_or_phone)
        print(password)
        user = User.objects.get(username=username_or_phone)
        print(user)
        print(user.check_password(password))
        if user is None or not user.check_password(password):
            return Response({"message": "Invalid Credentials"}, status=status.HTTP_403_FORBIDDEN)

        # real_otp_code = cache.get(user.phone_number)
        # if alg_otp_code != real_otp_code:
        #     return Response({'Error': 'otp code not right!'}, status=status.HTTP_403_FORBIDDEN)

        jwt_token = JWTAuthBackend.create_jwt(user)

        return Response({"token": jwt_token})


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, **kwargs):
        """
        Return a queryset of the user itself for the authenticated self.
        """
        print(self.kwargs.get('pk'))
        if isinstance(self.request.user, User):
            return User.objects.filter(id=self.kwargs.get('pk'))


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        data = request.data.copy()
        data['is_default'] = True

        user = request.user
        Address.objects.filter(user=user).exclude(id=instance.id).update(is_default=False)

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def get_queryset(self):
        """
        Return a queryset of all addresses for the authenticated user.
        """
        if isinstance(self.request.user,User):
            return Address.objects.filter(user=self.request.user)




@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def index(request):
    if request.user:
        return Response(f"Responseyou name is {request.user.username}")
    return Response("failed!")


@api_view(['POST'])
@csrf_exempt
@permission_classes([permissions.AllowAny])
def send_otp(request):
    serializer = OTPCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = User.objects.get(username=username)
    if user is None or not user.check_password(password):
            return Response({"message": "Invalid Credentials"}, status=status.HTTP_403_FORBIDDEN)

    if not user.phone_number:
        return Response({'error': 'Field required'}, status=status.HTTP_400_BAD_REQUEST)
    
    send_otp_code.delay(user.phone_number)
    

    return Response({'success':'OTP code sent!'}, status=200)


@api_view()
@permission_classes([permissions.IsAuthenticated])
def my_login(request):
    user = request.user
    
    if user:
        # Set User ID into session.
        request.session["member_id"] = user.id
        
        # Log in the authenticated user using Django's built-in login() method.
        django_request = request._request  # Get underlying HttpRequest from DRF Request instance.
        login(django_request, user)
        
        return Response(" You're logged in.")
    
    else:
        return Response("Your username and password didn't match.")



from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView


class RegisterViewSet(CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer


    def create(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'success': True, 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)