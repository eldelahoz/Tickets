import re
import os
# filecss = open('style.css', 'r')
# readcss = filecss.read()

# print(readcss)

def stylesincss():
	with open('css/style.css', 'r') as s:
		data = s.read()
		return data

print(stylesincss())