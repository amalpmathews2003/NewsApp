from django.shortcuts import render
from rest_framework.serializers import SerializerMetaclass
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

class UserSignUpReactView(APIView):

    serializer_class = UserReactSerializer
    def post(self, request):
        serializer = UserReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)
      



      
class ReactView(APIView):
    
    serializer_class = ReactSerializer
  
    def get(self, request):
        detail = [ {"name": detail.name,"detail": detail.detail} 
        for detail in React.objects.all()]
        return Response(detail)
  
    def post(self, request):
        #print(request.data)
        serializer = ReactSerializer(data=request.data)
      #  print(serializer)
        if serializer.is_valid(raise_exception=True):
            #print(serializer)
            serializer.save()
            return  Response(serializer.data)
        