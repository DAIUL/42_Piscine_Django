#!/usr/bin/python3

import requests
import sys
import json
import dewiki

BASE_URL = "https://fr.wikipedia.org/w/api.php"

def searchResult():

	query = sys.argv[1].strip().replace(" ", "_")
	query_params = {
		"action": "query",
		"list": "search",
		"srsearch": query,
		"format": "json"
	}

	try:
		response = requests.get(BASE_URL, params=query_params)
		response.raise_for_status()
		data = response.json()
		result = data.get("query", {}).get("search", [])
		if result:
			return result[0]["title"]
	except requests.exceptions.RequestException as e:
		print(f"Erreur lors de la requête : {e}")
	return None
	
def wikiFileCreate():

	title = searchResult()
	if not title:
		print("Error: no page found")
		return None

	query_params = {
		"action": "query",
		"format": "json",
		"prop": "extracts",
		"explaintext": True,
		"titles": title
	}

	try:
		response = requests.get(BASE_URL, params=query_params)
		response.raise_for_status()
		data = response.json()
	except requests.exceptions.RequestException as e:
		print(f"Erreur lors de la requête : {e}")
		return None
	
	pages = data.get("query", {}).get("pages", {})
	if not pages:
		print("Error: no page found")
		return None
	
	page = next(iter(pages.values()))
	if "missing" in page or "extract" not in page:
		print("Page not found or empty")
		return None

	content = page["extract"]
	title = title.strip().replace(" ", "_")

	with open(f"{title}.wiki", "w", encoding="utf-8") as f:
		f.write(content)

def main():

	if len(sys.argv) != 2:
		print("Utilisation: python3 request_wikipedia.py <research>")
		return

	wikiFileCreate()


if __name__ == '__main__':
	main()