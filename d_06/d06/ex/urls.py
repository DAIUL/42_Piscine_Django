from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name="ex00_homepage"),
	path('sign-up', views.sign_up, name="ex01_sign_up"),
	path('sign-in', views.sign_in, name="ex01_sign_in"),
	path('sign_out', views.sign_out, name="ex01_sign_out"),
	path('tips_upvote/<int:tip_id>/', views.tips_upvote, name="ex03_tips_upvote"),
	path('tips_downvote/<int:tip_id>/', views.tips_downvote, name="ex03_tips_downvote"),
	path('tips_delete/<int:tip_id>/', views.tips_delete, name="ex03_tips_delete"),
]
