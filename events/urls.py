from django.urls import path
from . import views

urlpatterns = [
    path("createEvent", views.add_main_event, name="Rejestracja"),
    path("details/<int:i>/", views.details_main_event, name="Detale"),
    path("edit/<int:i>/", views.edit_main_event, name="Detale"),
    path("delete/<int:i>/", views.delete_main_event, name="Usuniecie"),
    path("addSmallEvent/<int:i>/", views.add_small_event, name="Dodanie Small Event"),
    path("Register/<int:i>/", views.register_on_event, name="Zapis na Event"),
]
