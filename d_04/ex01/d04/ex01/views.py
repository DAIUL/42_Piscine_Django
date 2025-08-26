from django.shortcuts import render, HttpResponse

# Create your views here.
def django(request):
	return render(request, "base.html", {})

def affichage(request):
	return render(request, "base.html", {a voir})

def templates(request):
	return render(request, "base.html", {a voir})