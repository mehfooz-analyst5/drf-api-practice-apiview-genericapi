from django.db import models


# Create your models here.

class Student(models.Model):
    name  = models.CharField(max_length=255)
    roll  = models.CharField(max_length=50)
    department  = models.CharField(max_length=255)
    semester  = models.IntegerField()
    university  = models.CharField(max_length=255)
    campus  = models.CharField(max_length=255)

    def __str__(self):
        return str(f'{self.name} - {self.roll}')

