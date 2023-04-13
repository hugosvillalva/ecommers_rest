from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserlistSerializer, updateUserSerializer, PasswordSerializer
from rest_framework.decorators import action
from django.http import Http404



class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class = UserlistSerializer
    
    def get_object(self, pk):
        return self.serializer_class.Meta.model.objects.filter(id=pk)

    def get_queryset(self):
        if self.queryset is None:
            return self.serializer_class.Meta.model.objects.filter(is_active=True).values('id', 'username', 'email', 'password', 'name', 'last_name')
        return self.queryset

    #Sive para crear una ruta 
    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = User.objects.filter(id=pk).first()
        if not user:
            raise Http404
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({
                'message': 'Contraseña actualizada correctamente'
            })
        else:
            return Response(password_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def list(self, request):
        users = self.get_queryset()
        user_serializer = self.list_serializer_class(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': "Usuario creado correctamente"
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Ocurrio un error',
            'error': 'No se ha podido crear el usuario'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        user_destroy = User.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message': 'Usuario eliminado correctamente'
            })
        return Response({
            'message': 'No existe el usuario que desea eliminar'
        }, status=status.HTTP_400_BAD_REQUEST)

""" @api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    # retrieve object
    user = User.objects.filter(id=pk).first()
    # validation
    if user:
        # retrieve object
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        # update object
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete object
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': 'User deleted successfully!'}, status=status.HTTP_200_OK)
    # if object not found
    return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND) """
