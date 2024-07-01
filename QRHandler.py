import os, segno, cv2, copy
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageFont
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol


from Blakley import Blakley

class QRHandler:

    @staticmethod
    def generateQrCodesFromSecret(keys:list[int], p):
        key_str = []
        for key in keys:
            key_str.append('-'.join(map(str, key)))
        contador = 0
        qr_prime = QRHandler.__create_qr_code(p)
        # qr_prime.save('keys/normal/' + "prime.png")
        qr_prime.resize((300, 300)).save('keys/normal/' + "prime.png")
        for key in key_str:
            contador += 1
            qr_key = QRHandler.__create_qr_code(key)
            # qr_key.save('keys/normal/' + "key_" + str(contador) + '.png')
            qr_key.resize((300, 300)).save('keys/normal/' + "key_" + str(contador) + '.png')

            merged = QRHandler.__edit_qr_codes(qr_key, qr_prime)
            merged.save('keys/merged/' + "merged_key_" + str(contador) + '.png')
        # QRHandler.__create_qr_code(p, 'keys/' + "prime.png")
    
    @staticmethod
    def __create_qr_code(data):
        qrcode = segno.make_qr(data)
        return qrcode.to_pil()

    @staticmethod
    def __edit_qr_codes(key:Image, prime:Image):
        p = copy.deepcopy(prime)
        k = copy.deepcopy(key)
        k = k.resize((300, 300))
        p = p.resize((300, 300))

        font = ImageFont.truetype("Arial.ttf", 20)
        prime_text = "Prime"
        key_text = "Key Vector"

        left, top, right, bottom = font.getbbox(key_text)
        k_width = right - left
        k_height = bottom - top

        left, top, right, bottom = font.getbbox(prime_text)
        p_width = right - left
        p_height = bottom - top

        total_width = 300 * 2 + 20  # 20 pixels padding between QR codes
        total_height = max(k_width, p_width) + 300 + 20  # 20 pixels padding from the top
        new_image = Image.new('RGB', (total_width, total_height), (255, 255, 255))

        # Draw the titles
        draw = ImageDraw.Draw(new_image)
        k_x = (300 - k_width) // 2
        k_y = 10
        draw.text((k_x, k_y), key_text, fill=(0, 0, 0), font=font)
        
        p_x = 300 + 20 + (300 - p_width) // 2  # 20 pixels padding between QR codes
        p_y = 10  # 10 pixels padding from the top
        draw.text((p_x, p_y), prime_text, fill=(0, 0, 0), font=font)

        # Paste the scaled QR codes onto the new image
        qr_image1_y = max(k_height, p_height) + 20  # 20 pixels padding from the titles
        new_image.paste(k, (0, qr_image1_y))
        new_image.paste(p, (300 + 20, qr_image1_y))  # 20 pixels padding between QR codes
        return new_image


    @staticmethod
    def read_qr(filename):
        # Name of the QR Code Image file
        # filename = "scaled_qrcode.png"
        # read the QRCODE image
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        code = decode(image, symbols=[ZBarSymbol.QRCODE]) 
        if len(code) > 0 and not code[0].data is None:
            return code[0].data.decode('utf-8')


