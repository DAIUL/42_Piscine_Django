from django.shortcuts import render
from django.http import HttpResponse
from .models import Planets, People

def display(request):
	people = People.objects.filter(homeworld__climate__icontains="windy").select_related("homeworld").order_by("name")

	if not people.exists():
		return HttpResponse("No data available, please use the following command line before use:<br>"
            "<code>python manage.py loaddata ex09/ex09_initial_data.json</code>")
	
	return render(request, "planets_orm.html", {"people": people})