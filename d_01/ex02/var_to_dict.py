#!/usr/bin/python3

def	varToDict():

	d = [
		('Hendrix' , '1942'),
		('Allman' , '1946'),
		('King' , '1925'),
		('Clapton' , '1945'),
		('Johnson' , '1911'),
		('Berry' , '1926'),
		('Vaughan' , '1954'),
		('Cooder' , '1947'),
		('Page' , '1944'),
		('Richards' , '1943'),
		('Hammett' , '1962'),
		('Cobain' , '1967'),
		('Garcia' , '1942'),
		('Beck' , '1944'),
		('Santana' , '1947'),
		('Ramone' , '1948'),
		('White' , '1975'),
		('Frusciante', '1970'),
		('Thompson' , '1949'),
		('Burton' , '1939')
	]

	rev_dict = {}

	for name, date in d:
		if date not in rev_dict:
			rev_dict[date] = []
		rev_dict[date].append(name)

	for key, value in rev_dict.items():
		print(key, " : ", " ".join(value))

if __name__ == '__main__':
	varToDict()