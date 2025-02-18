from django.db import models

# Create your models here.

class AuthorModel(models.Model):
    name=models.CharField(max_length=25)
    bio=models.TextField()
    phone=models.IntegerField()

    def __str__(self):
        return self.name