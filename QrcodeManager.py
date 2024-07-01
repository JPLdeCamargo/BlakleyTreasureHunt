
# animated_qrcode.py

import segno
from urllib.request import urlopen
import cv2

#A escala influencia na decodificação ;-;
def createQrcode(info,filename):
    slts_qrcode = segno.make_qr(info)
    slts_qrcode.save(filename,scale = 5)
    # nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
    # slts_qrcode.to_artistic(
    #     background=nirvana_url,
    #     target="animated_qrcode.gif",
    #     scale=5,
    # )

def readQrcode(filename):
    # Name of the QR Code Image file
    # filename = "scaled_qrcode.png"
    # read the QRCODE image
    image = cv2.imread(filename)
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    # detect and decode
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    # if there is a QR code
    # print the data
    if vertices_array is not None:
        print("QRCode data:")
        print(data)
    else:
        print("There was some error") 

if __name__ == '__main__':
    filename = "qrcode.png"
    createQrcode("eba",filename)
    readQrcode(filename)