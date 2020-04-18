#pyzbar==0.1.8

from pyzbar.pyzbar import decode

from PIL import Image

# print(type(decode(Image.open('qrcode.png'))))
result = decode(Image.open('qrcode.png'))
print(result)

# for item in result:
#     print(type(item))
#     print(item)

print(result[0].data.decode('utf-8'))
