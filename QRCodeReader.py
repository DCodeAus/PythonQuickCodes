#pre prerequisite
#pip install pyqrcode
#pip install pypng

import pyqrcode
import png
from pyqrcode import QRCode

#string for the QR code
S = "www.geeksforgeeks.org"

#generate QR code
url = pyqrcode.create(S)

#create and save the svg file
url.svg("PythonQuickCodes/myqr.svg", scale = 8 )

#create and save the png file
url.png("PythonQuickCodes/myqr.png", scale = 6)