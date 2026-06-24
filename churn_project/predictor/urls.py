from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="dashboard", permanent=False)),
    path("predict/", views.predict, name="predict"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
