from django.shortcuts import render
from django.http import HttpResponse

def ex00(request):
	return render(request, "index.html")