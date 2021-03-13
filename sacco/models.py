from django.db import models

# Create your models here.
class SaccoManager(models.Model):
    Fname=models.CharField(max_length=10)
    Lname=models.CharField(max_length=10)
    Email=models.EmailField()
    Phone=models.IntegerField(max_length=10)
    # Id=models.FileField(max_length=10)

    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']