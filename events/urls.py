from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.Register, name="Rejestracja"),
    path("register/succes", views.suc, name="Powodzenie"),
    path("123", views.nr, name="Number")
]
