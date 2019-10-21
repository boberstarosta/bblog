from django.contrib import messages
from django.shortcuts import redirect, render

from users.forms import RegistrationForm


def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('users:login')
	else:
		form = RegistrationForm()
	return render(request, 'users/register.html', {'form': form})


def profile(request):
	return render(request, 'users/profile.html')