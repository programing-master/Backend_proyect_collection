from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
 
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, email=request.data["email"])
    if not user.check_password(request.data['password']):
        return Response({"error": "Invalid Password"}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializers(instance=user)
    return Response({'Token': token.key, 'user': serializer.data}, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def register(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializers(user)
    
    response = Response(serializer.data, status=status.HTTP_200_OK)
    # Incluye el token en las cabeceras de la respuesta
    response['Authorization'] = 'Token ' + token.key
    return response