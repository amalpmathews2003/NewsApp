from rest_framework import serializers
from . models import *
  
class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['name', 'detail']
    
class UserReactSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['name','email']