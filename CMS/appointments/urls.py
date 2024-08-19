from django.urls import path
from . import views

urlpatterns = [
    path("<int:appointment_id>/", views.appointment_detail, name="appointment_detail"),
]
