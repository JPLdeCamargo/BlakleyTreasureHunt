from blakley import Blakley
from KeyManager import generateQrCodesFromSecret, getKeysAndPfromQrcodes

def convert_int_to_utf8(num ):
    bin_string = bin(num)
    binary_int = int(bin_string, 2)
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    return binary_array.decode()

segredo = "pastel"
p = 5217712569307149314884997411507616511961101226671352088041037360428537519575582495381
blakley = Blakley(2,2,p)

generateQrCodesFromSecret(segredo,blakley)

keys, p = getKeysAndPfromQrcodes()
resp = blakley.decode(keys[:3])

print(convert_int_to_utf8(resp))


