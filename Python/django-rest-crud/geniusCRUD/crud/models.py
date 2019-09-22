from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField("Username", max_length=64,unique=True)
    email = models.EmailField("Email",max_length=255,unique=True)
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    password= models.CharField("Password",max_length=64)

    def __str__(self):
        return self.username


class Recipe(models.Model):
    name = models.CharField("Name of Recipe",  max_length=64,null=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.name


class Step_Model(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    step_text = models.CharField(max_length=64,null=False)
    
    def __str__(self):
        return self.step_text

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    text = models.CharField(max_length=64,null=False)
    
    def __str__(self):
        return self.text