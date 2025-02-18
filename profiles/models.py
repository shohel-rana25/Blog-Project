from django.db import models
from author.models import AuthorModel
# Create your models here.

class ProfileModel(models.Model):
    name=models.CharField(max_length=20)
    about=models.TextField()
    author=models.OneToOneField(AuthorModel, on_delete=models.CASCADE,  null=True, blank=True)

    def __str__(self):
        return self.name