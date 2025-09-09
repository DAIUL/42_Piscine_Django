from django.shortcuts import render

def tab(request):
	rows = []
	steps = 50
	for i in range(1, steps + 1):
		ratio = int(255 * i / steps)
		black = f"rgb({ratio},{ratio},{ratio})"
		red   = f"rgb({ratio},0,0)"
		green = f"rgb(0,{ratio},0)"
		blue  = f"rgb(0,0,{ratio})"
		rows.append([black, red, green, blue])
	return render(request, "tab.html", {"rows": rows})