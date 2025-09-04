from django import forms

class HistoryForm(forms.Form):
	texte = forms.CharField(
		label = "Bodycount ?",
		max_length= 100)