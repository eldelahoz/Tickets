import re
import os

def stylesincss():
	"""
	This function returns the styles.css as plain text:

	Returns:
		data: read fille styles.css
	"""
	cwd = os.getcwd()
	with open(cwd+'/modules/css/style.css', 'r') as s:
		data = s.read()
		return data