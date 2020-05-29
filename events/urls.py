from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.add_main_event, name="Rejestracja"),
    path("register/succes", views.suc, name="Powodzenie"),
    path("details/<int:i>/", views.details_main_event, name="Detale"),
    path("edit/<int:i>/", views.edit_main_event, name="Detale"),
    path("delete/<int:i>/", views.delete_main_event, name="Usuniecie"),
    path("addSmallEvent/<int:i>/", views.add_small_event, name="Dodanie Small Event"),
]
