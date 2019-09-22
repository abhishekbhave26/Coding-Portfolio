from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,Recipe,Ingredient,Step_Model
from .serializers import UserSerializer,RecipeSerializer,Step_ModelSerializer,IngredientSerializer

# Create your views here.
class UserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RecipeAPIView(APIView):
    
    def get_object(self):
        try:
            return Recipe.objects.all()
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
             

    def delete(self, request, pk, format=None):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class IngredientAPIView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class Step_ModelAPIView(generics.ListCreateAPIView):
    queryset = Step_Model.objects.all()
    serializer_class = Step_ModelSerializer