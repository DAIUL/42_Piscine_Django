from django.urls import path
from . import views

urlpatterns = [
	path("", views.ex00, name="Ex00 : Markdown Cheatsheet.")
]