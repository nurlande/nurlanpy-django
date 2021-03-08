# serializers.py
from rest_framework import serializers

from .models import Registration
from .models import User

class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = ('id','fullName', 'phoneNumber', 'address', 'inn')
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','userName', 'password')
