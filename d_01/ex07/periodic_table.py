#!/usr/bin/python3

import sys


def periodicTab():

	periodic_tab = []

	with open("periodic_table.txt", "r", encoding="utf-8") as file:
		for line in file:

			element_values = {}
			element_name, properties = line.split(" = ")
			element_values["name"] = element_name
			pairs = properties.split(", ")

			for pair in pairs:
				key, value = pair.split(":")
				element_values[key.strip()] = value.strip()

			periodic_tab.append(element_values)

	return periodic_tab

def elementGenerator(element: dict) -> str:

	elements_html = f"""		<td> 
		<h4>{element['name']}</h4> 
		<ul> 
			<li>{element['number']}</li>
			<li>{element['small']}</li>
			<li>{element['molar']}</li>
		</ul>
	</td>"""
	
	return elements_html

def htmlGenerator():

	periodic_tab = periodicTab()

	html_elements = []

	for element in periodic_tab:
		html_elements.append(elementGenerator(element))

	table_body = "\n".join(html_elements)

	html_content = f"""
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Periodic Table</title>
	</head>
	<body>
		<table>
		{table_body}
		</table>
	</body>
	</html>
	"""

	with open("periodic_table.html", "w", encoding="utf-8") as file:
		file.write(html_content)

if __name__ == '__main__':
	htmlGenerator()