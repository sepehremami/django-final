from django.contrib.auth.views import LoginView
from django.shortcuts import render
from apps.cart.models import OrderInfo, CartDiscount
from apps.user.backends import JWTAuthBackend
from apps.user.models import User, Address
from django.contrib.auth.views import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from apps.user.tasks import send_otp_code
from .serializers import (
    AddressPostSerializer,
    ObtainTokenSerializer,
    UserRegisterSerializer,
    UserSerializer,
    AddressSerializer,
    OTPCodeSerializer,
    ChangePasswordSerializer,
)
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions, views as api_views
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
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
        auth_cookie = request.COOKIES.get("access")
        if auth_cookie is None:
            return redirect(reverse("landing"))
        return super().dispatch(request, *args, **kwargs)


from apps.user.forms import UpdateUserForm
from jwt import decode

class ProfileView(AuthenticationRequiredMixin, TemplateView):
    model = User
    template_name = "user/profile.html"

    def get(self, *args, **kwargs):
        id = kwargs.get("pk")
        user = User.objects.get(pk=id)
        user_update_form = UpdateUserForm(instance=user)
        context = self.get_context_data()
        context["user_form"] = user_update_form
        return render(self.request, "user/profile.html", context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        if isinstance(user, User):
            addresses = Address.objects.filter(user=user)
            context["addresses"] = addresses
            orders = OrderInfo.objects.filter(user=user)
            context["orders"] = orders
        return context


# TODO: write otp authentication back
class ObtainTokenView(ObtainAuthToken):
    permission_classes = [permissions.AllowAny]
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer: ObtainTokenSerializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
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
            return Response(
                {"message": "Invalid Credentials"}, status=status.HTTP_403_FORBIDDEN
            )

        jwt_token = JWTAuthBackend.create_jwt(user)

        return Response({"token": jwt_token})


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, **kwargs):
        """
        Return a queryset of the user itself for the authenticated self.
        """
        print(self.kwargs.get("pk"))
        if isinstance(self.request.user, User):
            return User.objects.filter(id=self.kwargs.get("pk"))


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        data = request.data.copy()
        data["is_default"] = True

        user = request.user
        Address.objects.filter(user=user).exclude(id=instance.id).update(
            is_default=False
        )

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def get_queryset(self):
        """
        Return a queryset of all addresses for the authenticated user.
        """
        if isinstance(self.request.user, User):
            return Address.objects.filter(user=self.request.user, is_deleted=False)


    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create':
            return AddressPostSerializer
        return AddressSerializer


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def index(request):
    if request.user:
        return Response(f"Responseyou name is {request.user.username}")
    return Response("failed!")


@api_view(["POST"])
@csrf_exempt
@permission_classes([permissions.AllowAny])
def send_otp(request):
    serializer = OTPCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    phone = serializer.validated_data.get("phone")
    send_otp_code.delay(phone)
    return Response({"success": "OTP code sent!"}, status=200)


from .serializers import OTPValidCodeSerializer


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def validate_opt(request):
    serializer = OTPValidCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    otp = serializer.validated_data.get("otp_code")
    otp_code = request.data.get("otp_code")
    phone = request.data.get("phone")
    real_otp_code = cache.get(phone)

    if otp_code != real_otp_code:
        print("h")
        return Response(
            {"Error": "otp code not right!"}, status=status.HTTP_403_FORBIDDEN
        )

    user = User.objects.get(phone_number=phone)
    if user is None:
        print("k")
        return Response(
            {"message": "Invalid Credentials"}, status=status.HTTP_403_FORBIDDEN
        )

    jwt_token = JWTAuthBackend.create_jwt(user)
    return Response({"token": jwt_token})


@api_view()
@permission_classes([permissions.IsAuthenticated])
def my_login(request):
    user = request.user

    if user:
        request.session["member_id"] = user.id

        django_request = request._request
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
            return Response(
                {"success": True, "user_id": user.id}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.generics import UpdateAPIView


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartTemplateView(AuthenticationRequiredMixin, TemplateView):
    model = get_user_model()
    template_name = 'cart/cart.html'

    def get_context_data(self, *args, **kwargs):
        user = kwargs.get('pk')
        print('pk', user)
        orders = OrderInfo.objects.get(user_id=user, order_status=2)
        print('orders', orders)
        context = super().get_context_data()
        context['cart'] = orders
        return context


class FinalOrderTemplateView(AuthenticationRequiredMixin, TemplateView):
    model = get_user_model()
    template_name = 'cart/order.html'

    def get_context_data(self, *args, **kwargs):
        user = kwargs.get('pk')
        print('pk', user)
        orders = OrderInfo.objects.get(user_id=user, order_status=2)
        print('orders', orders)
        context = super().get_context_data()
        context['cart'] = orders
        return context

