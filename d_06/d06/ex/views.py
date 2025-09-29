from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import random, time
from .forms import SignUpForm, SignInForm, TipForm
from .models import UserInfos, Tip

def homepage(request):
	tips = Tip.objects.all().order_by("created_at")
	if request.user.is_authenticated:
		form = TipForm(request.POST or None)
		if request.method == "POST" and form.is_valid():
			tip = form.save(commit=False)
			tip.author = request.user
			tip.save()
			return redirect("ex00_homepage")
	else:
		form = None

	return render(request, "homepage.html", {"tips": tips, "form": form})

def sign_up(request):
	if request.user.is_authenticated:
		return redirect("ex00_homepage")
	
	if request.method == "POST":
		form = SignUpForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			
			return redirect("ex00_homepage")
	
	else:
		form = SignUpForm()

	return render(request, "sign_up.html", {"form": form})

def sign_in(request):
	if request.user.is_authenticated:
		return redirect("ex00_homepage")

	if request.method == "POST":
		form = SignInForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect("ex00_homepage")
	else:
		form = SignInForm()

	return render(request, "sign_in.html", {"form": form})

def sign_out(request):
	logout(request)
	return redirect("ex00_homepage")

@login_required(login_url="ex01_sign_in")
def tips_upvote(request, tip_id):
	tip = get_object_or_404(Tip, id=tip_id)
	user = request.user

	if request.method == "POST":
		if user in tip.upvotes.all():
			tip.upvotes.remove(user)
		else:
			tip.upvotes.add(user)
		
		if user in tip.downvotes.all():
			tip.downvotes.remove(user)

	return redirect("ex00_homepage")

@login_required(login_url="ex01_sign_in")
def tips_downvote(request, tip_id):
	tip = get_object_or_404(Tip, id=tip_id)
	user = request.user

	if request.method == "POST":
		if user.has_perm("ex.downvote_tip") or user == tip.author or user.score_calculation() > 15:
			if user in tip.downvotes.all():
				tip.downvotes.remove(user)
			else:
				tip.downvotes.add(user)	
			if user in tip.upvotes.all():
				tip.upvotes.remove(user)

			if tip.downvoted_count() >= 3:
				tip.delete()

	return redirect("ex00_homepage")

@login_required(login_url="ex01_sign_in")
def tips_delete(request, tip_id):
	tip = get_object_or_404(Tip, id=tip_id)
	user = request.user

	if request.method == "POST":
		if user == tip.author or user.has_perm('ex.delete_tip') or user.score_calculation() > 30:
			tip.delete()

	return redirect("ex00_homepage")