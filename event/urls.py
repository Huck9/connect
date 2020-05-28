from django.urls import path
from . import views

urlpatterns = [
    path('', views.showevent, name='showEvent'),
    path('addEvent/', views.addevent, name='addRvent'),
]
