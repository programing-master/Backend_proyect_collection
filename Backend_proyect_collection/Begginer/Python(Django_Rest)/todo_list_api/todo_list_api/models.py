from django.db import models
from .validators import validate_data

# Create your models here.
class TaskModel(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField();
    urgency = models.CharField(validators=[validate_data])
    created_at=models.DateTimeField(auto_now_add=True)