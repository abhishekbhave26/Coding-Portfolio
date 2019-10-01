from rest_framework import serializers
from .models import Recipe,Step,Ingredient

class RecipeSerialize(serializers.Serializer):
    class Meta:
        model = Recipe
        fields = "__all__"

class StepSerialize(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"

class IngredientSerialize(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"