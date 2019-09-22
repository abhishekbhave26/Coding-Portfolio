"""geniusCRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    # Get event
    path('recipe/' r'^(?P<pk>\d+)/$', views.RecipeAPIView.as_view(),name='create_recipe'),
    # list all events
    path('recipe/' r'^list/$', views.RecipeAPIView.as_view(),name='list_recipe'),
    # url(r'^update$/(?P<pk>\d+)', #update event),
    path('recipe/' r'^create/$', views.RecipeAPIView.as_view(),name='create_recipe'),
    # delete event
    path('recipe/' r'^delete$/(?P<pk>\d+)',views.RecipeAPIView.as_view(), name='delete_recipe'),

    path('admin/', admin.site.urls),
    path('recipe/',views.RecipeAPIView.as_view(), name='recipe-list'),
    path('user/', views.UserAPIView.as_view(), name='user-list'),
    path('step_model/', views.Step_ModelAPIView.as_view(), name='step_model-list'),
    path('ingredient/', views.IngredientAPIView.as_view(), name='ingredient-list')
    
]
