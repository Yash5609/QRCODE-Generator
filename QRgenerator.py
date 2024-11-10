import pyqrcode
from pyqrcode import QRCode

#link which represent QRcode
link = "https://www.youtube.com/watch?v=Ckf1X6-3qVI" 

#generate QRcode
url = pyqrcode.create(link)

#create and save QR
url.svg('youtube.svg' , scale = 8)

