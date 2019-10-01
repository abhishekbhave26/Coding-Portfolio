from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^createrecipe/', views.createRecipe),
    url(r'^getrecipe/(?P<user>\w{0,50})/$', views.getRecipeOfGivenUser),
    url(r'^updaterecipe/', views.updateRecipe),
    url(r'^deleterecipe/(?P<recipe>\w{0,50})/$', views.deleteRecipe),
]