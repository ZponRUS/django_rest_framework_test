from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
	#path('user/new/', UserCreateView.as_view()),
	#path('user/all/', UserListView.as_view()),
	#path('user/detail/<int:pk>/', UserDetailView.as_view()),

	path('user/', UserViewSet.as_view({'get':'list'})),
	path('user/new/', UserViewSet.as_view({'post':'create'})),
	path('user/<int:pk>/', UserViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
]
