from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment, Note
from .forms import NoteForm


@login_required
def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    notes = appointment.notes.all()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.appointment = appointment
            note.author = request.user
            note.save()
            return redirect("appointment_detail", appointment_id=appointment.id)
    else:
        form = NoteForm()
    return render(
        request,
        "appointments/appointment_detail.html",
        {"appointment": appointment, "notes": notes, "form": form},
    )
