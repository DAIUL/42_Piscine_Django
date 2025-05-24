#!usr/bin/python3

import random
import beverages as brvg

class CoffeeMachine:

	def __init__(self):
		self.service_count = 0

	class EmptyCup(brvg.HotBeverage):
		def __init__(self):
			super().__init__()
			self.name = "empty cup"
			self.price = 0.90

		def description(self):
			return "An empty cup?! Gimme my money back!"
	
	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		self.service_count = 0
		print("Machine repaired")

	def serve(self, cls):
		if self.service_count < 10:
			drink = random.choice([cls, CoffeeMachine.EmptyCup])
			drink_served = drink()
			if isinstance(drink_served, CoffeeMachine.EmptyCup):
				print(drink_served.description())
			else:
				self.service_count += 1
				print(f"A {drink_served.name} has been served")
			return drink_served
		else:
			raise CoffeeMachine.BrokenMachineException


def main():

	machine = CoffeeMachine()
	crash_count = 0

	while crash_count < 2:
		try:
			machine.serve(random.choice([brvg.Cappuccino, brvg.Cappuccino, brvg.Coffee, brvg.Tea, brvg.HotBeverage]))
		except CoffeeMachine.BrokenMachineException as e:
			print(e)
			machine.repair()
			crash_count += 1

if __name__ == '__main__':
	main()