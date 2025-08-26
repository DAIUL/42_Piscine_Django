from django.urls import path
from . import views

urlpatterns = [
	path('django', views.django, name="Ex01 : Django, framework web."),
	path('affichage', views.affichage, name="Ex01 : Processus d’affichage d’une page statique."),
	path('templates', views.templates, name="Ex01 : Moteur de template."),
]
