from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from apps.user.models import User


class ObtainTokenSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "username"]
