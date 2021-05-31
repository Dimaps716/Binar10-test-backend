"""Api view"""
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import UserSerializer
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet

# list all users
# @api_view(['GET'])
# def usersList(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)


# # bring users by id
# @api_view(['GET'])
# def usersDetail(request, pk):
#     users = User.objects.get(id=pk)
#     serializer = UserSerializer(users, many=False)
#     return Response(serializer.data)

# # create users
# @api_view(['POST'])
# def usersCreate(request):
#     serializer = UserSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# # update users 
# @api_view(['POST'])
# def usersUpdate(request, pk):
#     users = User.objects.get(id=pk)
#     serializer = UserSerializer(instance=users, data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

class UserViewSet(FlexFieldsModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
