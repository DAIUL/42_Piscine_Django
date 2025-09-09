from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def index(request):
    try:
        res = requests.get('https://www.markdownguide.org/cheat-sheet/')
        res.raise_for_status()
    except requests.HTTPError as e:
        return HttpResponse(e)
    soup = BeautifulSoup(res.text, 'html.parser')
    content_div = soup.find("div", class_="col-xs-12 col-sm-12 col-md-9")
    content = [str(tag) for tag in soup.find_all(["h1", "h2", "h3", "table"])]
    return render(request, 'index.html', {'content' : content})