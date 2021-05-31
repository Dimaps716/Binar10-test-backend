"""Api view"""
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import UserSerializer
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# list all items
@api_view(['GET'])
def itemsList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# bring items by id
@api_view(['GET'])
def itemsDetail(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

# create items
@api_view(['POST'])
def itemsCreate(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# update items 
@api_view(['POST'])
def itemsUpdate(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(instance=users, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)