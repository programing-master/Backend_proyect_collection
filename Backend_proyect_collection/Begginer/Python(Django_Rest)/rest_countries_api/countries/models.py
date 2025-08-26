from django.db import models

# Create your models here.
class CountriesModel(models.Model):
    img=models.TextField()
    completed_name=models.TextField()
    sovereignty=models.TextField()
    capital = models.CharField(max_length=255, blank=True)
    continent = models.CharField(max_length=255, blank=True)
    
    
    def __str__(self):
        return self.completed_name