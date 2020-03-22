from etich import Etich
import cgi
form = cgi.FieldStorage()
number = form.getfirst('number')
compy = ' '.join(form.getlist('compy'))
name = ' '.join(form.getlist('name'))
sku = ' '.join(form.getlist('sku'))
field = ' '.join(form.getlist('field'))

users_etich = Etich(compy, name, sku, field).save_etich()
