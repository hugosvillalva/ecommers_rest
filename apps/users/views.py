from datetime import datetime
from django.contrib.sessions.models import Session  
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken


from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.api.serializers import CustomObtainPairSerializer,CustomUserSerializer
from apps.users.models import User

#Login With JWT
class Login(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        userername = request.data.get('username', "")
        password = request.data.get("password", "")
        user = authenticate(
            username = userername,
            password = password
        )

        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token' : login_serializer.validated_data.get('access'),
                    'refresh_token' : login_serializer.validated_data.get('refresh'),
                    'user' : user_serializer.data,
                    'message' : 'Inicio Existoso'
                }, status= status.HTTP_202_ACCEPTED)
            return Response({
                'error' : 'Contraseña o nombre de usuarios incorrectos'
            }, status= status.HTTP_400_BAD_REQUEST) 
        return Response({
            'error' : 'Contraseña o nombre de usuarios incorrectos'
        }, status= status.HTTP_400_BAD_REQUEST)


#Logout with JWT
class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id = request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({
                'message': 'Sesion cerrada correctamente'
            }, status= status.HTTP_202_ACCEPTED)
        return Response({
            'error': 'No se a encontrado un usuario con esa ID'
        }, status= status.HTTP_400_BAD_REQUEST)

#Login and logout in token
""" class Usetoken(APIView):
    authentication_classes = [ExpiringTokenAuthentication]

    def get(self, request, *args, **kwargs):
        try:
            # Obtener el token de autenticación del usuario actual
            user_token = Token.objects.get(user=request.user)
            user = UserTokenSerializer(request.user)
            return Response({
                'token' : user_token.key,
                'user' : user.data
            })
        except Token.DoesNotExist:
            return Response({
                'error' : 'El usuario no tiene un token de autenticación válido'
            }, status= status.HTTP_400_BAD_REQUEST)


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # Se corrige la sintaxis del nombre de la variable de login_serializer a login_serializer
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if login_serializer.is_valid():
            # Se corrige la sintaxis para obtener el usuario validado
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso.'
                    }, status=status.HTTP_201_CREATED)
                else:
                    token.delete()
                    return Response({
                        'error': 'Ya se ha iniciado Sesion con este usuario'
                    },status= status.HTTP_401_UNAUTHORIZED
                    )
            else:
                return Response({
                    'error': 'Este usuario no puede iniciar sesión.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'error': 'Nombre de usuario o contraseña incorrectos.'
            }, status=status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):
    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                session_message = 'Sesiones de usuario Eliminadas'
                token.delete
                token_message = 'token eliminado'
                return Response({
                    'token_message':token_message,
                    'session_message': session_message
                    
                }, status= status.HTTP_200_OK)
            return Response({
                'error': 'No se ha encontrado un usuario con estas credenciales'
            }, status= status.HTTP_400_BAD_REQUEST)
        except:
            return Response({
                'error' : 'No se a encontrado Token en la peticion'
            }, status= status.HTTP_409_CONFLICT) """