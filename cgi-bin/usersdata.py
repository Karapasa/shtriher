#!/usr/bin/python3
from etich import Etich
import cgi
# Сбор данных из URL
form = cgi.FieldStorage()
number = form.getfirst('number')
compy = ' '.join(form.getlist('compy'))
name = ' '.join(form.getlist('name'))
sku = ' '.join(form.getlist('sku'))
field = ' '.join(form.getlist('field'))

users_etich = Etich(number, compy, name, sku, field).save_etich()

print("Status: 200 OK")
print("Content-Type: text")
print()
