from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length = 30, null = False, blank = False)
    id = models.IntegerField(primary_key = True, blank = False, null = False)
    department = models.CharField(max_length = 20, null = False, blank = False)
    salary = models.DecimalField(max_digits = 10, decimal_places = 2)
    
    def __str__(self):
        return self.id