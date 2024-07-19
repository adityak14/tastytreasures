from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(max_length=200, default='')
    ingredients = models.TextField(default='')

    def __str__(self):
        return self.title
