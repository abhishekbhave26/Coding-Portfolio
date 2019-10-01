from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    name = models.CharField("Name of Recipe",  max_length=64,null=False)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Step(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    step_text = models.CharField(max_length=64,null=False)
    
    def __str__(self):
        return self.step_text

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    text = models.CharField(max_length=64,null=False)
    
    def __str__(self):
        return self.text