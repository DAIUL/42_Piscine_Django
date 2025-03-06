#!/usr/bin/python3

def read_num():

	with open("numbers.txt", "r") as file:
		content = file.readline().strip()
		numbers = content.split(",")

	for number in numbers:
		print(number)

if __name__ == '__main__':
	read_num()