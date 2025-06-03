#!/usr/bin/python3

from path import Path

def main():

	p = Path("test_dir") / "test_file.txt"

	p.parent.mkdir_p()

	p.write_text("Bravo ca fonctionne, tu veux une medaille ?")

	print("File content:", p.read_text())

if __name__ == '__main__':
	main()