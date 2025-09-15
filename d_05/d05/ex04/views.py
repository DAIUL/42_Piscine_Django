from django.shortcuts import render
import psycopg2
from django.conf import settings
from django.http import HttpResponse
from django.db import IntegrityError
import os

def init(request):
	
	try:
		conn = psycopg2.connect(
			dbname="formationdjango",
			user="djangouser",
			password="secret",
			host="localhost",
		)
		cur=conn.cursor()

		query="""
		CREATE TABLE IF NOT EXISTS ex04_movies (
			title VARCHAR(64) UNIQUE NOT NULL,
			episode_nb INT PRIMARY KEY,
			opening_crawl TEXT,
			director VARCHAR(32) NOT NULL,
			producer VARCHAR(128) NOT NULL,
			release_date DATE NOT NULL
		);
		"""

		cur.execute(query)
		conn.commit()
		
		cur.close()
		conn.close()
		return HttpResponse("OK")
	
	except Exception as e:
		return HttpResponse(f"Error: {e}")

def populate(request):
	data = [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19",
        },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16",
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19",
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25",
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kutz, Rick McCallum",
            "release_date": "1980-05-17",
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25",
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J. J. Abrams",
            "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "release_date": "2015-12-11",
        },
    ]
	results = []
	
	try:
		conn = psycopg2.connect(
            dbname="formationdjango",
            user="djangouser",
            password="secret",
            host="localhost",
        )
		cur = conn.cursor()

		for film in data:
			try:
				cur.execute(
                    """
                    INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                    VALUES (%s, %s, %s, %s, %s);
                    """,
                    (
                        film["episode_nb"],
                        film["title"],
                        film["director"],
                        film["producer"],
                        film["release_date"],
                    ),
                )
				results.append(f"{film['title']}: OK")
			except Exception as e:
				results.append(f"{film['title']}: {str(e)}")
				conn.rollback()
			else:
				conn.commit()

		cur.close()
		conn.close()
	except Exception as e:
		return HttpResponse(f"Database error: {e}")

	return HttpResponse("<br>".join(results))


def display(request):
    try:
        conn = psycopg2.connect(
            dbname="formationdjango",
            user="djangouser",
            password="secret",
            host="localhost",
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM ex04_movies;")
        rows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]  # noms des colonnes

        cur.close()
        conn.close()

        if not rows:
            return HttpResponse("No data available")

        return render(request, "movies_sql.html", {
            "columns": colnames,
            "rows": rows,
        })

    except Exception as e:
        return HttpResponse(f"Database error: {e}")
	
def remove(request):
	try:
		conn = psycopg2.connect(
        	dbname="formationdjango",
        	user="djangouser",
        	password="secret",
        	host="localhost",
		)
		cur = conn.cursor()

		if request.method == "POST":	
			title = request.POST.get("title")
			if title:
				cur.execute("DELETE FROM ex04_movies WHERE title = %s;", [title])
				conn.commit()

		cur.execute("SELECT title FROM ex04_movies;")
		titles = cur.fetchall()
		movies = [t[0] for t in titles]
			
		cur.close()
		conn.close()
	
		if not movies:
			return HttpResponse("No data available")
		
		return render(request, "remove_sql.html", {"movies": movies})
	
	except Exception as e:
		return HttpResponse("No data available")
	
