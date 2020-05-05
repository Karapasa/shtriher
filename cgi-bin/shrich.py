#!/usr/bin/python3
import barcode
from barcode.writer import ImageWriter

class Code():

    CODE = 'ean13'
    def_number = '460311009062'

    def __init__(self, number, type='ver', width=0.2, height=20):
        self.type = type
        self.number = number
        self.width = width
        self.height = height
        self.name = "/var/www/html/label/img/"+number+"_sht"

    def get_number(self):
        return self.number

    def get_code(self):
        return self.CODE

    def generate(self):
        num = self.get_number()
        cod = self.get_code()
        return barcode.get(cod, num, writer=ImageWriter())

    def save_code(self):
        ean = self.generate()
        ean.save(self.name,
                 options={'background': 'white', 'module_width': 0.4, 'module_height': 20, 'foreground': 'black',
                          'text_distance': 1, 'font_size': 11})


if __name__ == '__main__':
    a1 = Code(Code.def_number)
    a1.save_code()
    print('Штрихкод сохранен')
