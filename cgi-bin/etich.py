#!/usr/bin/python3
from PIL import Image, ImageDraw, ImageFont
from shrich import Code

def_number = '123412412341'
compy = 'Рога и компыта'
sku = 'A1234B'
name = 'Рюкзак Космос'
field = 'Принт - Сатурн'


class Etich():
    font = ImageFont.truetype("DejaVuSansMono.ttf", size=18, encoding='utf-8')

    def __init__(self, number, compy, name, sku, field, view = 'ver', width = 120, height = 75):
        self.number = number
        self.view = view
        self.width = width
        self.height = height
        self.compy = compy
        self. name = name
        self. sku = sku
        self.field = field
    def get_company(self):
        return 'Название компании: ' + self.compy
    def get_sku(self):
        return 'Артикул: ' + self.sku
    def get_name(self):
        return 'Наименование продукции: ' + self.name
    def get_field(self):
        return 'Описание: ' + self.field
    def get_shtrich(self):
        a1 = Code(self.number)
        a1.save_code()

    def create_etich(self):
        img = Image.new('RGBA', (455, 284), 'white')
        idraw = ImageDraw.Draw(img)
        data = (self.get_company(), self.get_name(), self.get_sku(), self.get_field())
        x, y = 40, 25
        for text in data:
            idraw.text((x, y), text, font=self.font, fill='black')
            y += 25
        self.get_shtrich()
        sht = Image.open('/var/www/html/label/img/'+self.number+'_sht.png', 'r').resize((250, 120))

        img.paste(sht, (102, 150))
        return img

    def save_etich(self):
        img = self.create_etich()
        img.save('/var/www/html/label/img/'+self.number+'_et.png')
if __name__ == '__main__':
    a2 = Etich(def_number, compy, name, sku, field).save_etich()
    print('Этикетка и штрихкод сохранена')
