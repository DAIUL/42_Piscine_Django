from django.shortcuts import render
from .forms import HistoryForm
from django.utils.timezone import now
from django.conf import settings
import os

def history(request):
	log_file = settings.LOG_FILE_PATH

	if not os.path.exists(log_file):
		with open(log_file, "w", encoding="utf-8") as f:
			f.write("")

	with open(log_file, "r", encoding="utf-8") as f:
		history = f.readlines()

	if request.method == "POST":
		form = HistoryForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data["texte"]
			timestamp = now().strftime("%Y-%m-%d %H:%M:%S")
			entry = f"[{timestamp}] {text}\n"
			with open(log_file, "a", encoding="utf-8") as f:
				f.write(entry)
			history.append(entry)
	else:
		form = HistoryForm()

	return render(request, "history.html", {"form": form, "history": history})