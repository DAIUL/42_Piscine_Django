#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://en.wikipedia.org/wiki/"

def get_first_paragraph(soup):
    content = soup.find('div', id='mw-content-text')
    paragraphs = content.find_all('p', recursive=True)

    for p in paragraphs:
        if p.text.strip():
            return p
    return None

def roads_to_philo(query, philosophy_path):

	try:
		response = requests.get(f"{BASE_URL}{query}")
		response.raise_for_status()
		soup = BeautifulSoup(response.text, 'html.parser')
	except requests.exceptions.RequestException as e:
		print(f"Error: Error during the request {e}")
		return None
	
	title = soup.find('h1').text
	print(title)

	if title in philosophy_path:
		print("It leads to an infinite loop !")
		return
	
	philosophy_path.append(title)

	if title.strip() == "Philosophy":
		philosophy_path.append(title)
		return

	content = soup.find('div', id='mw-content-text')
	paragraphs = content.find_all('p', recursive=True)

	for p in paragraphs:
		if p.text.strip():
			for link in p.find_all('a'):
				href = link.get('href')
				if href.startswith("/wiki/") and ':' not in href:
					next_link = href.split("/wiki/")[1]
					roads_to_philo(next_link, philosophy_path)
					return
		
	print("It leads to a dead end !")
	return


def main():

	if len(sys.argv) != 2:
		print("Utilisation: python3 roads_to_philosophy.py <research>")
		return None
	
	query = sys.argv[1].strip()

	philosophy_path = []

	roads_to_philo(query, philosophy_path)
	if "Philosophy" in philosophy_path:
		print(f"{len(philosophy_path)} roads from {query} to philosophy")

if __name__ == '__main__':
	main()