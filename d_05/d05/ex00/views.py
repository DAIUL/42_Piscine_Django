from django.shortcuts import render
import psycopg2
from django.conf import settings
from django.http import HttpResponse

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
		CREATE TABLE IF NOT EXISTS ex00_movies (
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