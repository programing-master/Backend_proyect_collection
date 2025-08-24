from rest_framework import viewsets,permissions
from .models import TaskModel
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
     queryset=TaskModel.objects.all()
     permission_classes=[permissions.AllowAny]
     serializer_class=TaskSerializer;
     