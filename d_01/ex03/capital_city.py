#!/usr/bin/python3

import sys

def	giveCapital():

	if len(sys.argv) != 2:
		sys.exit(0)

	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}

	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	state_name = states.get(sys.argv[1])

	print(capital_cities.get(state_name, "Unknown state"))

if __name__ == '__main__':
	giveCapital()