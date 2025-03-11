#!/usr/bin/python3

import sys


def periodicTab():

	periodic_tab = []

	with open("periodic_table.txt", "r", encoding="utf-8") as file:
		for line in file:

			element_values = {}
			element_name, properties = line.split(" = ")
			pairs = properties.split(", ")

			for pair in pairs:
				key, value = pair.split(":")
				element_values[key.strip()] = value.strip()

			element = {element_name: element_values}
			periodic_tab.append(element)

	return periodic_tab

def htmlGenerator():

	periodic_tab = periodicTab()

	html_content = f"""
	"""

	with open("periodic_table.html", "w", encoding="utf-8") as file:
		file.write(html_content)

if __name__ == '__main__':
	periodicTab()