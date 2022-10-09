#pip install Pillow
#pip install qrcode
import qrcode
from PIL import Image
Logo_link='googlelogo.jpg'

#image for centre of QR code
logo = Image.open(Logo_link)

#base width of 100
basewidth=100

#adjusting image size
wpercent=(basewidth/float(logo.size[0]))
hsize=int((float(logo.size[1]*float(wpercent))))
logo=logo.resize((basewidth,hsize), Image.ANTIALIAS)
QRcode=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

#url or text for QR code
url = 'https://www.google.com/'

#adding URL or text to the QR code
QRcode.add_data(url)

#generate QR code
QRcode.make()

#input colour of QR code
QRcolor='#89E8F6'

#add colour to QR code
QRimg=QRcode.make_image(fill_color=QRcolor, back_color='white').convert('RGB')

#set size of QR code
pos =((QRimg.size[0]-logo.size[0]) // 2,
        (QRimg.size[1]-logo.size[1]) // 2)
QRimg.paste(logo, pos)

#save QR code as Name
QRimg.save('QRCodeName.png')

print ('QR code generated!')

