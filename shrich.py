import barcode
from barcode.writer import ImageWriter

class Code():

    CODE = 'ean13'
    number = '460311009062'

    def __init__(self, type='ver', width=0.2, height=20):
        self.type = type
        self.width = width
        self.height = height
        self.name = "testname"

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
        print('Штрихкод сохранен')


if __name__ == '__main__':
    a1 = Code()
    a1.save_code()
