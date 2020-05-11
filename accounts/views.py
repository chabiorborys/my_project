from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views import View
from project.models import Profile
from accounts.forms import UserForm

class SignUpView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            birth_date = form.cleaned_data['birth_date']
            blood = form.cleaned_data['blood_type']
            pesel = form.cleaned_data['pesel']
            Profile.objects.create(user=user, birth_date=birth_date, blood=blood, pesel=pesel)
            return redirect('/')
        return render(request, 'registration.html', {'form': form})