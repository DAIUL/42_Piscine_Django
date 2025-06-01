#!/usr/bin/pyhton3

from elements import *

ALLOWED_CLASS_IN_HTML = (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)

ALLOWED_CLASS_IN_DIV_BODY = (Table, Ul, Ol, H1, H2, Div, Span, Text)

class Page():

	def __init__(self, element):
		if not isinstance(element, Elem):
			raise TypeError("Not the good type")
		self.element = element
	

	def is_valid(self, element=None):
		if element is None:
			element = self.element

		if not isinstance(element, ALLOWED_CLASS_IN_HTML):
			return False
		
		if isinstance(element, Elem):
			for child in element.content:
				if not self.is_valid(child):
					return False
		
		if isinstance(element, Html):
			if len(element.content) != 2:
				return False
			if not isinstance(element.content[0], Head) and not isinstance(element.content[1], Body):
				return False
		
		if isinstance(element, Head):
			if len(element.content) != 1 or not isinstance(element.content[0], Title):
				return False
			
		if isinstance(element, (Div, Body)):
			if not all(isinstance(child, ALLOWED_CLASS_IN_DIV_BODY) for child in element.content):
				return False
		
		if isinstance(element, (Title, H1, H2, Li, Th, Td)):
			if len(element.content) != 1 or not isinstance(element.content[0], Text):
				return False
			
		if isinstance(element, P):
			if not all(isinstance(child, Text) for child in element.content):
					return False

		if isinstance(element, Span):
			if not all(isinstance(child, (Text, P)) for child in element.content):
					return False
			
		if isinstance(element, (Ol, Ul)):
			if len(element.content) < 1 or not all(isinstance(child, Li) for child in element.content):
				return False
			
		if isinstance(element, Tr):
			if len(element.content) < 1 or not ((all(isinstance(child, Th) for child in element.content) or (all(isinstance(child, Td) for child in element.content)))):
				return False
			
		if isinstance(element, Table):
			if not all(isinstance(child, Tr) for child in element.content):
				return False
		
		return True
			
	def __str__(self):
		if isinstance(self.element, Html):
			return f"<!DOCTYPE html>\n{self.element}"
		else:
			return f"{self.element}"

def test():
	try:
		print(Page(Body()))
	except Html.ValidationError as e:
		print(e)

if __name__ == '__main__':
	test()