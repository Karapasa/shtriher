import barcode
from barcode.writer import ImageWriter
from barcode import get


code = 'ean13'
number = '123456789101'
def get_shtrih(code,number):
    return get(code, number, writer=ImageWriter())
def save_shtrih():
    ean1 = get_shtrih(code, number)
    ean1.save('testean3', options={'background':'white', 'module_width':0.2, 'module_height':10, 'foreground':'black', 'text_distance':1.0, 'font_size': 18 })
    print('Штрихкод сохранен')

if __name__ == '__main__':
    save_shtrih()
