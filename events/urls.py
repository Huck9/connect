from django.urls import path
from . import views

urlpatterns = [
    path("createEvent", views.add_main_event, name="utworzenie Event"),
    path("details/<int:i>/", views.details_main_event, name="Detale Event"),
    path("edit/<int:i>/", views.edit_main_event, name="Edycja Event"),
    path("delete/<int:i>/", views.delete_main_event, name="Usuniecie Event"),
    path("addSmallEvent/<int:i>/", views.add_small_event, name="Dodanie Small Event"),
    path("deleteSmallEvent/<int:i>/", views.delete_small_event, name="Usuniecie Small Event"),
    path("editSmallEvent/<int:i>/", views.edit_small_event, name="Edycja Small Event"),    
    path("details/<int:i>/register", views.register_to_event, name="registertoevent"),
    path("addopinionevent/<int:i>", views.add_opinion, name="add opinion"),
    path("deleteopinion/<int:i>", views.deleteOpinion, name="add opinion"),
]
