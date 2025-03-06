#!/usr/bin/python3

import sys

def	giveState():

	if len(sys.argv) != 2:
		sys.exit(0)

	states = {
		"Oregon" : "OR",
		"Alabama" : "AL", "New Jersey": "NJ",
		"Colorado" : "CO"
	}

	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	state_code = next((key for key, value in capital_cities.items() if value == sys.argv[1]), "Unknown state")
	
	print(next((key for key, value in states.items() if value == state_code), "Unknown state"))
	
if __name__ == '__main__':
	giveState()