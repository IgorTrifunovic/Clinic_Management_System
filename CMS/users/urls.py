from django.urls import path
from .views import register_patient, profile

urlpatterns = [
    path('register/', register_patient, name='register_patient'),
    path('profile/', profile, name='profile'),
]
