from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
import random, time
from .forms import SignUpForm, SignInForm
from .models import UserInfos

def homepage(request):
	return render(request, "homepage.html")

def sign_up(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			
			return redirect("ex00_homepage")
	
	else:
		form = SignUpForm()

	return render(request, "sign_up.html", {"form": form})

def sign_in(request):
	if request.method == "POST":
		form = SignInForm(request.POST)
		if form.is_valid():
			user = authenticate(
					request,
					username=form.cleaned_data.get("username"),
					password=form.cleaned_data.get("password")
				)

			if user is not None:
				login(request, user)
				return redirect("ex00_homepage")
			else:
				form.add_error(None, "Invalid username or password")

	else:
		form = SignInForm()

	return render(request, "sign_in.html", {"form": form})

def sign_out(request):
	logout(request)
	return redirect("ex00_homepage")