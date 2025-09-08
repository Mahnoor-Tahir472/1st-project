from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User


class SignUpAPI(APIView):
    def post(self, request):
        username=request.data.get('username')
        password=request.data.get('password')

        if not username or not password :
            return Response({"error": "username and password are required"}, status=400)
        
        if User.objects.filter(username=username).exists():
            return Response({"Message": "user name already exist"},status=400)
         
        user=User.objects.create_user(username=username , password=password )
        return Response({"Message":"user created succesfully"},status=201)
