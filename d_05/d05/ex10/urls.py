from django.urls import path
from . import views

urlpatterns = [
	path('', views.search, name="ex10_search")
]
