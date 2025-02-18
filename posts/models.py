from django.db import models
from categories.models import CategoryModel
from author.models import AuthorModel

# Create your models here.

class PostModel(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    categroy=models.ManyToManyField(CategoryModel)
    author=models.ForeignKey(AuthorModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title