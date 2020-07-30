from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UsersListSerializer
from .models import User

# Create your views here.

'''
class UserCreateView(generics.CreateAPIView):
	serializer_class = UserDetailSerializer

class UserListView(generics.ListAPIView):
	serializer_class = UsersListSerializer
	queryset = User.objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = UserDetailSerializer
	queryset = User.objects.all()
'''

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UsersListSerializer
    queryset = User.objects.all()	