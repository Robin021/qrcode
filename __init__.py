#-*- coding: utf-8 -*-
import qrcode
import datetime,time
import hashlib
import random
from PIL import Image



searchip = '211.151.113.206'
searchtime = '1985-12-13'
zhichashi = '11130000001003'
peiliao = '福鼎大白毫'
guige = ''
commpany = '福建省福鼎市茶禅一品茶业有限公司'

print('请输入产品名称:')
name = input()

print('请输入配料名称:')
peiliao = input()

print('请输入规格:')
guige = input()

print('请输入年份(2016-05-06):')
year = input()

print('请输入产地:')
address = input()

print('请输入制茶师编号:')
zhichashi = input()

print('请输入溯源:')
comments = input()

print('输入本批次产品数量:')
x = input()
number = 1
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
now = time.strftime("%Y%m%d%H%M%S")


def record_to_txt(now, number, passwd, name, brand, address, comments, year , zhichashi , peiliao , guige):
    with open('db/qr.txt', 'a',encoding='utf-8') as f:
        f.write(now + str(number) + '|' + passwd + '|' + '0' + '|' + name + '|' + brand + '|' + address + '|' + comments + '|' + year + '|' + searchip + '|' + searchtime + '|' + zhichashi + '|' + peiliao + '|' + guige + '\n')


for number in range(int(x)):
    passwd = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=7,
    )
    qr.add_data('http://www.xyz.com/qrcode/qrcode.php?product=' + now + str(number) + '&md5=' + passwd)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    icon = Image.open("img/logo.png")
    icon_w, icon_h = icon.size

    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.convert("RGBA")
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    txticon = Image.open("img/txt.png")
    txticon_w, txticon_h = txticon.size
    txticon = txticon.convert("RGBA")
    txticon_w = img_w
    txticon_h = 30
    txticon = txticon.resize((txticon_w, txticon_h), Image.ANTIALIAS)
    img.paste(icon, (w, h), icon)
    img.paste(txticon,(0, 192), txticon)
#    img.show()
    img.save('qrcode/' + name + '/' + now + str(number) + '.png')
    record_to_txt(now, number, passwd, name, commpany, address, comments, year, zhichashi, peiliao, guige)
    number += 1
    print(number)

