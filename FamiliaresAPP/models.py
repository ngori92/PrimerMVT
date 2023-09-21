from django.db import models

# Create your models here.
class Familiar(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    birth_date = models.DateField()
    is_alive = models.BooleanField()
    address = models.CharField(max_length=50)
    
    
    