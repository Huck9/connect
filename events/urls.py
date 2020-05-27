from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("rejestruj/", views.Register, name="Rejestracja"),
    path("rejestruj/succes", views.suc, name="Powodzenie"),
    path("123", views.nr, name="Number")
]
