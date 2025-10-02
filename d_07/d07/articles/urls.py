from django.urls import path
from .views import ArticleListView, UserLoginView, HomeRedirectView, UserCreateView, PublicationListView, ArticleDetailView, FavouritesListView, PublishCreateView, AddFavouriteCreateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
	path('', HomeRedirectView.as_view(), name="home"),
	path('articles', ArticleListView.as_view(), name="articles"),
	path('login', UserLoginView.as_view(template_name="login.html"), name="login"),
	path('publications', PublicationListView.as_view(), name="publications"),
	path('details/<int:pk>', ArticleDetailView.as_view(), name="details"),
	path('favourites', FavouritesListView.as_view(), name="favourites"),
	path('logout', LogoutView.as_view(next_page="home"), name="logout"),
	path('register', UserCreateView.as_view(), name="register"),
	path('publish', PublishCreateView.as_view(), name="publish"),
	path('articles/<int:pk>/add-favorite/', AddFavouriteCreateView.as_view(), name='add_favourite'),
]
