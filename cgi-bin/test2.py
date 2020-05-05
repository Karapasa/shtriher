#!/usr/bin/python3

import cgi

form = cgi.FieldStorage()
num = form.getfirst('number')
sec = ' '.join(form.getlist('second'))
three = ' '.join(form.getlist('three'))
four = ' '.join(form.getlist('four'))

data = [num, sec, three, four]

print("Content-Type: text/html; charset=utf-8")
print()
print("Hello World!")
print("<br>")
print(data)
