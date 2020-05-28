from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="Rejestracja"),
    path("register/succes", views.suc, name="Powodzenie"),

]
