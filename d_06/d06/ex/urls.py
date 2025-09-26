from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name="ex00_homepage"),
	path('sign-up', views.sign_up, name="ex01_sign_up"),
	path('sign-in', views.sign_in, name="ex01_sign_in"),
	path('sign_out', views.sign_out, name="ex01_sign_out"),
]
