from django.shortcuts import render
from rest_framework import viewsets
from users.models import users
from users.serializers import user_serializers
# Create your views here.

class user_view(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = user_serializers
