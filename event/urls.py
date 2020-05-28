from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='Events'),
    path('addEvent/', views.add_event, name='addRvent'),
]
