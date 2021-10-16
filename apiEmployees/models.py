from django.db import models

# Create your models here.
class Employees (models.Model):
    name = models.CharField(max_length=100)
    prename = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_naiss = models.DateField()

    def __str__(self):
        return self.name
    