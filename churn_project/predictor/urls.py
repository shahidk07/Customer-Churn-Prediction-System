from django.urls import path
from . import views

urlpatterns = [
    path("collect_data/", views.collect_data, name="collect_data"),
    path("predict/", views.predict, name="predict"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
