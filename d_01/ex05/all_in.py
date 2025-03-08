#!/usr/bin/python3

import sys

def	giveAll():

	if len(sys.argv) != 2 or not isinstance(sys.argv[1], str):
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

	infos = [info.strip() for info in sys.argv[1].split(",") if info.strip()]

	states_lower = {k.lower(): v for k, v in states.items()}

	capital_lower = {k: v.lower() for k, v in capital_cities.items()}

	for info in infos:
		if info.lower() in states_lower:
			state_code = states_lower.get(info.lower())
			print(capital_cities.get(state_code), "is the capital of", (next(k for k, v in states.items() if v == state_code)))
		elif info.lower() in capital_lower.values():
			state_code = next(k for k, v in capital_lower.items() if info.lower() == v)
			print(capital_cities.get(state_code), "is the capital of ", (next(k for k, v in states.items() if v == state_code)))
		else:
			print(info, "is neither a capital city nor a state")
			
			
	
if __name__ == '__main__':
	giveAll()