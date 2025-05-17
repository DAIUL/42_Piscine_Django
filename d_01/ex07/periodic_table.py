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

def orderTab(periodic_tab: dict):

	empty_tab = [["" for _ in range(18)] for _ in range(7)]

	line = 0

	for element in periodic_tab:
		empty_tab[line][int(element["position"])] = elementGenerator(element)
		if int(element["position"]) == 17:
			line += 1

	return empty_tab
		

def htmlGenerator():

	periodic_tab = periodicTab()

	html_elements = orderTab(periodic_tab)

	table_body = ""

	for row in html_elements:
		table_body += "<tr>\n"
		for cell in row:
			if cell:
				table_body += f"{cell}\n"
			else:
				table_body += "\t<td></td>\n"
		table_body += "</tr>\n"

	css_content = f"""
	@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');

	* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
	font-family: Roboto, sans-serif;
	}}

	td {{
	border: 1px solid black;
	padding: 10px;
	}}
	"""

	html_content = f"""
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" href="periodic_table.css">
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

	with open("periodic_table.css", "w", encoding="utf-8") as file:
		file.write(css_content)

if __name__ == '__main__':
	htmlGenerator()