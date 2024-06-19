from django.db import models
from django.conf import settings

class Appointment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='patient_appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='doctor_appointments', on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.CharField(max_length=255)
    # Add more fields as needed

    def __str__(self):
        return f"{self.patient.username} - {self.date}"

class Note(models.Model):
    appointment = models.ForeignKey(Appointment, related_name='notes', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note by {self.author.username} on {self.created_at}"
