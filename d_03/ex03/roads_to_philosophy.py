#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://en.wikipedia.org/wiki/"

def roads_to_philo(query, philosophy_path):

	try:
		response = requests.get(f"{BASE_URL}{query}")
		response.raise_for_status()
		soup = BeautifulSoup(response.text, 'html.parser')
	except requests.exceptions.RequestException as e:
		print(f"Error: Error during the request {e}")
		return None
	
	if query in philosophy_path:
		print("Loop detected!")
		return

	if soup.find('h1').text.strip() == "Philosophy":
		philosophy_path.append(soup.find('h1').text)
		return

	first_p = soup.find('div', id='mw-content-text').find('p')
	if first_p is None:
		print("No paragraph found.")
		return

	for link in first_p.find_all('a'):
		href = link.get('href')
		if href.startswith("/wiki/") and ':' not in href:
			philosophy_path.append(soup.find('h1').text)
			next_link = href.split("/wiki/")[1]
			roads_to_philo(next_link, philosophy_path)
			return

def main():

	if len(sys.argv) != 2:
		print("Utilisation: python3 roads_to_philosophy.py <research>")
		return None
	
	query = sys.argv[1].strip()

	philosophy_path = []

	roads_to_philo(query, philosophy_path)
	print(philosophy_path)

if __name__ == '__main__':
	main()