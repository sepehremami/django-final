import datetime
from apps.shop.models import Category
from apps.shop.serializer import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

class CategoryAPIListView(APIView):
    