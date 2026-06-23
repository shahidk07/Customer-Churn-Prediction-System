from django.urls import path
from . import views

urlpatterns = [
    path("predict/", views.predict, name="predict"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
