from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
 
from .serializer import TaskSerializer
from .models import Task

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class RegisterUser(APIView):
    def post(self, request, *args, **kwargs):
	username = request.data.get('username', '')
	password = request.data.get('password', '')
	email = request.data.get('email', '')

	if not username o not password or not email:		
	    return Response({'error': 'Username, password and email are required'}, status=status.HTTP_400_BAD_REQUEST)

	if User.object.filter(username= username).exists():
            return Response({'error': 'Username is already in use'}, status=status.HTTP_400_BAD_REQUEST)

	# Here need to add validations for password, remember
	
	user = User.objects.create_user(username=username, email=email)
	user.set_password(password)
	user.save()

	return Response({'detail': 'User created successfully'}, status=status.HTTP_201_CREATED)
