from django.shortcuts import render
from django.http import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializer import UserSerializer

# Create your views here.


@api_view(['GET'])
def home(request):
    return Response('home is working')


@api_view(['POST'])
def signup(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['pass']
    user = User.objects.create(
        username=username,
        email=email,
        password=password
    )
    userSerializer=UserSerializer(user, many=False)
    return Response(userSerializer.data)


@api_view(['POST'])
def signin(request):
    # return Response('signin is working')
    username = request.data['username']
    password = request.data['pass']
    try:
        user = User.objects.get(username=username)
        if user.password == password:
            return Response('you are logged in')
        else:
            return Response('credential error')
    except User.DoesNotExist as e:
        return Response('user does not exist')

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    userSerializer = UserSerializer(users, many=True)
    return Response(userSerializer.data)
