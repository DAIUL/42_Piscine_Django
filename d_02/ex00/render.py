#!usr/bin/python3

import sys
import os
import re

if len(sys.argv) != 2:
	print("Usage: python3 render.py <file.template>")
	sys.exit(1)

file = sys.argv[1]

if not file.endswith(".template") or not os.path.exists(file):
	print("Error: file must end with .template")
	sys.exit(1)

with open(file, "r", encoding="utf-8") as f:
	file_content = f.read()

settings = {}

with open("settings.py", "r", encoding="utf-8") as f:
	for line in f:
		key, value = line.split("=", 1)
		settings[key.strip()]= value.strip().strip('"').strip("'")

re.sub(r"\{.*?\}", replaceVariable, templateText)