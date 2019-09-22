from rest_framework import serializers

from .models import User,Recipe,Step_Model,Ingredient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"
        
class Step_ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step_Model
        fields = "__all__"

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"