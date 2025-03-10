#!/usr/bin/python3

def mySort():
	
	d={
	'Hendrix' : '1942',
	'Allman' : '1946',
	'King' : '1925',
	'Clapton' : '1945',
	'Johnson' : '1911',
	'Berry' : '1926',
	'Vaughan' : '1954',
	'Cooder' : '1947',
	'Page' : '1944',
	'Richards' : '1943',
	'Hammett' : '1962',
	'Cobain' : '1967',
	'Garcia' : '1942',
	'Beck' : '1944',
	'Santana' : '1947',
	'Ramone' : '1948',
	'White' : '1975',
	'Frusciante': '1970',
	'Thompson' : '1949',
	'Burton' : '1939',
	}

	date_dict = {}

	for name, date in d.items():
		if date not in date_dict:
			date_dict[date] = []
		date_dict[date].append(name)

	for date in sorted(date_dict):
		for name in sorted(date_dict[date]):
			print(name)


if __name__ == '__main__':
	mySort()