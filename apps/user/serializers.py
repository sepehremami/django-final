import re
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from apps.user.models import User
from rest_framework import viewsets
from .models import Address


class ObtainTokenSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()
  otp_code = serializers.CharField()


class OTPCodeSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "username", "email", "first_name", "last_name", "phone_number"]


class AddressSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Address
    fields = ['id', 'user','receiver','province','city','addr','zip_code','phone','is_default']

  def validate_zipcode(self, value):
    pattern = r'^\d{5}$'
    
    if not bool(re.match(pattern, value)):
      raise serializers.ValidationError('Invalid zip code format')

    



