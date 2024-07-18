from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# RegisterUser maneja el registro de usuarios
class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        email = request.data.get('email', '')

        # Verificar si faltan campos obligatorios
        if not username or not password or not email:
            return Response({'error': 'Username, password and email are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar si el nombre de usuario ya está en uso
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already in use'}, status=status.HTTP_400_BAD_REQUEST)

        # Se puede agregar validación adicional de la contraseña aquí

        # Crear un nuevo usuario
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        return Response({'detail': 'User created successfully'}, status=status.HTTP_201_CREATED)


# Vista para manejar el inicio de sesión de usuarios
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Logs detallados para debugging
        print('Request Headers:', request.headers)
        print('Request Data:', request.data)

        username = request.data.get('username')
        password = request.data.get('password')

        # Si no existe usuario o password en request
        if not username or not password:
            print('Missing username or password')
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Autenticar usuario
        user = authenticate(request, username=username, password=password)
        print('Authenticated User:', user)

        if user is not None:
            print(user, 'useeeeer', password, 'passworrrrd')
            # Iniciar sesión del usuario
            login(request, user)
            # Generar token de refresco
            refresh = RefreshToken.for_user(user)
            # Obtener token CSRF
            csrf_token = get_token(request)
            print('Generated CSRF Token:', csrf_token)

            response = Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
            # Establecer cookie CSRF
            response.set_cookie('csrftoken', csrf_token, httponly=False, samesite='Lax')
            print('Set-Cookie Header:', response.cookies)  # Verificar la cookie
            return response
        else:
            print('Invalid credentials')
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# Vista para manejar el cierre de sesión de usuarios
class LogoutView(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        # Cerrar sesión del usuario
        logout(request)
        
        # Crear una respuesta de éxito
        response = Response(
            {
                'message': 'Logout successful',
                'code': 200,
                'status': 1
        })
        
        # Eliminar la cookie CSRF
        response.delete_cookie('csrftoken')
        
        # Devolver la respuesta de éxito
        return response

@csrf_exempt
def get_csrf_token(request):
    # Generar token CSRF
    csrf_token = get_token(request)
    print('Generated CSRF Token:', csrf_token)  # Verificar el token
    return JsonResponse({'csrfToken': csrf_token})
