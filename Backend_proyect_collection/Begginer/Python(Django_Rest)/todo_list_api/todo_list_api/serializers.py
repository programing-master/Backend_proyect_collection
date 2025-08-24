from .models import TaskModel
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
   class Meta:  
     model=TaskModel;
     fields=('title','description','urgency','created_at');
     fields_only_read=('created_at',)