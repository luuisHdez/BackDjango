from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt

from .serializer import TaskSerializer
from .models import Task

# TaskView sets up the viewset for CRUD operations on Task instances
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

# RegisterUser handles user registration
class RegisterUser(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        email = request.data.get('email', '')

        if not username or not password or not email:
            return Response({'error': 'Username, password and email are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already in use'}, status=status.HTTP_400_BAD_REQUEST)

        # Additional password validation can be added here

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        return Response({'detail': 'User created successfully'}, status=status.HTTP_201_CREATED)

# View to handle user login
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            response = Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
            response.set_cookie('csrftoken', get_token(request), httponly=True, samesite='Lax')
            return response
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# View to handle user logout
@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        response = Response({'detail': 'Logout successful'})
        response.delete_cookie('csrftoken')
        return response
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)