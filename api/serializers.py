from rest_framework import serializers
from .models import User

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


'''
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
'''