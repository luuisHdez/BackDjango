from rest_framework.views import APIView
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