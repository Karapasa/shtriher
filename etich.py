from PIL import Image, ImageDraw, ImageFont
sht = Image.open('testean3.png', 'r')

img = Image.new('RGBA', (450, 300), 'white')
idraw = ImageDraw.Draw(img)

text='Название компании - ООО Рога и копыта'
font = ImageFont.truetype("arial.ttf", size=18, encoding='utf-8')

idraw.text((20, 20), text, font=font, fill='black')
img.paste(sht, (30,90))

img.save('test_etick.png')
