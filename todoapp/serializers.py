from rest_framework import serializers
from todoapp.models import Task

class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Task
        fields = '__all__' 
