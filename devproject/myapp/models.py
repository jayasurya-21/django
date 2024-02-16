from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_lenght=100)
    email = models.EmailField()
    contact = models.CharField(max_lenght=15)
     
    class Meta:
         db_table = "tbemployee"   