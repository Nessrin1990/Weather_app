from . import views
from django.urls import path,include
urlpatterns = [
    path("",views.index),
    path('home', views.home, name='home'),

]
