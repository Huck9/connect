from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="Rejestracja"),
    path("register/succes", views.suc, name="Powodzenie"),
    path("details/<int:i>/", views.details, name="Detale"),
    path("edit/<int:i>/", views.edit, name="Detale"),
    path("delete/<int:i>/", views.delete, name="Usuniecie")
]
