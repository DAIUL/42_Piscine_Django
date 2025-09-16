from django.shortcuts import render
import psycopg2
from django.conf import settings
from django.http import HttpResponse
from django.db import IntegrityError

def get_connection():
	return psycopg2.connect(
		dbname="formationdjango",
		user="djangouser",
		password="secret",	
		host="localhost",
	)

def init(request):
	
	try:
		conn = get_connection()
		cur=conn.cursor()

		cur.execute("""
			CREATE TABLE IF NOT EXISTS ex08_planets (
				id SERIAL PRIMARY KEY,
				name VARCHAR(64) UNIQUE NOT NULL,
				climate VARCHAR(32),
				diameter INT,
				orbital_period INT,
				population BIGINT,
				rotation_period INT,
				surface_water REAL,
				terrain VARCHAR(128)
			);
			CREATE TABLE IF NOT EXISTS ex08_people (
				id SERIAL PRIMARY KEY,
				name VARCHAR(64) UNIQUE NOT NULL,
				birth_year VARCHAR(32),
				gender VARCHAR(32),
				eye_color VARCHAR(32),
				hair_color VARCHAR(32),
				height INT,
				mass REAL,
				homeworld VARCHAR(64) REFERENCES ex08_planets(name)
			);
		""")
		conn.commit()
		
		cur.close()
		conn.close()
		
		return HttpResponse("OK")
	
	except Exception as e:
		return HttpResponse(f"Error: {e}")

def populate(request):
	try:
		conn = get_connection()
		cur = conn.cursor()

		with open("ex08/data/planets.csv", "r") as f:
			cur.copy_from(f, "ex08_planets", sep="\t", null="NULL", columns=("name", "climate", "diameter", "orbital_period", "population", "rotation_period", "surface_water", "terrain"))
		conn.commit()

		with open("ex08/data/people.csv", "r") as f:
			cur.copy_from(f, "ex08_people", sep="\t", null="NULL", columns=("name", "birth_year", "gender", "eye_color", "hair_color", "height", "mass", "homeworld"))
		conn.commit()

		cur.close()
		conn.close()
	
		return HttpResponse("OK")

	except Exception as e:
		return HttpResponse(f"No data available")


def display(request):
	try:
		conn = get_connection()
		with conn.cursor() as cur:
			cur.execute("""
				SELECT p.name, p.homeworld, pl.climate
				FROM ex08_people p
				JOIN ex08_planets pl ON p.homeworld = pl.name
				WHERE pl.climate ILIKE '%windy%'
				ORDER BY p.name ASC;
			""")
			rows = cur.fetchall()
			colnames = [desc[0] for desc in cur.description]

		conn.close()

		if not rows:
			return HttpResponse("No data available")

		return render(request, "planets_sql.html", {
			"columns": colnames,
			"rows": rows,
		})

	except Exception as e:
		return HttpResponse("No data available")