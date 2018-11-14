from django.db import models

# Create your models here.
class Form(models.Model):
    username=models.CharField(max_length=65)
    email=models.EmailField()


    def __str__(self):
        return self.username