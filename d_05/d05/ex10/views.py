from django.shortcuts import render
from .models import Movies, People, Planets

def search(request):
	movies = Movies.objects.all()
	people = People.objects.all()
	planets = Planets.objects.all()
	selection = []
	genders = People.objects.values_list("gender", flat=True).distinct().order_by

	if request.method == "POST":
		min_date = request.POST.get("min_date")
		max_date = request.POST.get("max_date")
		diameter = request.POST.get("diameter")
		gender = request.POST.get("gender")

		if min_date:
			movies = movies.filter(release_date__gte=min_date)
		if max_date:
			movies = movies.filter(release_date__lte=max_date)
		
		if diameter:
			planets = planets.filter(diameter__gt=diameter)

		if gender:
			people = people.filter(gender__iexact=gender)

		if gender:
			selection = movies.filter(characters__in=people).distinct()

	return render(request, "manytomany.html", {
				"movies": movies,
				"people": people,
				"planets": planets,
				"selection": selection,
				"genders": genders
				})