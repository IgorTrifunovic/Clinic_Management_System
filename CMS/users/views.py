from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import PatientRegistrationForm, ProfileForm
from .forms import PatientRegistrationForm
from django.contrib.auth.decorators import login_required

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to profile page or homepage
    else:
        form = PatientRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileForm(request.POST, instance=request.user.profile, user=request.user)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile')
    else:
        p_form = ProfileForm(instance=request.user.profile, user=request.user)
    return render(request, 'users/profile.html', {'p_form': p_form})
