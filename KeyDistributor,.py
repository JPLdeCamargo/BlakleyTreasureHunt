from blakley import Blakley
import QrcodeManager
import os
def generateKeysFromSecret(secret ):
    secret_bytes = secret.encode("utf-8")
    secretInt = int.from_bytes(secret_bytes)

    p = 5217712569307149314884997411507616511961101226671352088041037360428537519575582495381
    x0 = secretInt
    a = 2   
    b = 2
    w = Blakley.encode(a, b, p, x0)
    return w 



if __name__ == '__main__':
    segredo = "eba"
    keys = generateKeysFromSecret(segredo)
    keyStr = []
    for key in keys:
        keyStr.append('-'.join(map(str,key)))
    
    contador = 0
    for key in keyStr:
        contador +=1
        QrcodeManager.createQrcode(key,'keys/'+"key_"+str(contador) + '.png')

    qrCodes = os.listdir('keys')
    for name in qrCodes:
        QrcodeManager.readQrcode("keys/"+name)