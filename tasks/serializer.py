from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)  # Ajusta el formato según sea necesario
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)  # Ajusta el formato según sea necesario

    class Meta:
        model = Task
        fields = '__all__'