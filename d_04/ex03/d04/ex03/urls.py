from django.urls import path
from . import views

urlpatterns = [
	path('', views.tab, name="ex03_tab")
]
