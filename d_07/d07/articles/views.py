from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, RedirectView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import UserFavoriteArticle, Article
from .forms import ArticleForm

class ArticleListView(ListView):
	model = Article
	template_name = "articles.html"
	context_object_name = "articles"
	ordering = ['-created']

class PublicationListView(LoginRequiredMixin, ListView):
	model = Article
	template_name = "publications.html"
	context_object_name = "publications"
	login_url = "login"

	def get_queryset(self):
		return Article.objects.filter(author=self.request.user)

class HomeRedirectView(RedirectView):
	url = reverse_lazy("articles")

class UserLoginView(LoginView):
	template_name= "login.html"

class UserCreateView(CreateView):
	model = User
	form_class = UserCreationForm
	template_name = "register.html"
	success_url = reverse_lazy("login")

class ArticleDetailView(DetailView):
	model = Article
	template_name = "details.html"
	context_object_name = "article"

	def post(self, request, *args, **kwargs):
		article = self.get_object()
		user = request.user
		if user.is_authenticated:
			UserFavoriteArticle.objects.get_or_create(user=user, article=article)
		return redirect('details', pk=article.id)

class FavouritesListView(LoginRequiredMixin, ListView):
	model = UserFavoriteArticle
	template_name = "favourites.html"
	context_object_name = "favourites"
	login_url = "login"

	def get_queryset(self):
		return UserFavoriteArticle.objects.filter(user=self.request.user)
	
class PublishCreateView(LoginRequiredMixin, CreateView):
	model = Article
	form_class = ArticleForm
	template_name = "publish.html"
	success_url = reverse_lazy("publications")

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
class AddFavouriteCreateView(LoginRequiredMixin, CreateView):
	model = UserFavoriteArticle
	fields = []
	template_name = "add_favourite.html"
	login_url = "login"

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.article = get_object_or_404(Article, pk=self.kwargs['pk'])
		return super().form_valid(form)
	
	def get_success_url(self):
		return reverse_lazy("details", kwargs={"pk": self.kwargs['pk']})
	