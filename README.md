Package contains two Python QR code generator programs.
Comments are within the python files for reference.
1. pictureQRCodeGenerator.py
Installation of two packages must be done before hand
First two lines are the packages that need to be installed through running the command in the comments:
pip install Pillow
pip install qrcode
Line 5 is the logo link, this pulls the logo image from the folder of the project 'PythonQuickCodes'
Line 20 is the url required for the QR code to point to.
Line 32 is for the user to set the backround color and line 29 mentions the colour of the QR code to be filled with, default set as black.
The QR code is then saved as default name QRCodeName.png
And prints a message when complete.


2. QRCodeGenerator.py
Installation of two packages must be done before hand
First two lines are the packages that need to be installed through running the command in the comments:
pip install pyqrcode
pip install pypng

This program is simple in that it only needs a URL or string for the QR code.
The user then receives two outputs: one file in .png format and one file in .svg