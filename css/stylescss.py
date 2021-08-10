import re
import os

def stylesincss():
	"""
	This function returns the styles.css as plain text:

	Returns:
		data: read fille styles.css
	"""
	with open('css/style.css', 'r') as s:
		data = s.read()
		return data