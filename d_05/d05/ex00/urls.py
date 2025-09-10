from . import views
from django.urls import path

urlpatterns = [
	path('init', views.init, name='ex00_init'),
]
