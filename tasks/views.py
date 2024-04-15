from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

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
