from blakley import Blakley
import QrcodeManager
import os
def generateKeysFromSecret(secret, blakley: Blakley):
    secret_bytes = secret.encode("utf-8")
    secretInt = int.from_bytes(secret_bytes)
    x0 = secretInt

    w = blakley.encode(x0)
    return w 

def generateQrCodesFromSecret(secret,blakley: Blakley):
    keys = generateKeysFromSecret(secret,blakley)
    keyStr = []
    for key in keys:
        keyStr.append('-'.join(map(str, key)))
    contador = 0
    for key in keyStr:
        contador += 1
        QrcodeManager.createQrcode(key, 'keys/' + "key_" + str(contador) + '.png')
    QrcodeManager.createQrcode(blakley.p, 'keys/' + "p.png")


def getKeysAndPfromQrcodes():
    qr_code_folder = os.listdir('keys')
    keys = []
    for name in qr_code_folder:
        data = QrcodeManager.readQrcode("keys/" + name)
        if data:

            if 'key' in name:
                    dataArray = data.split('-')
                    keys.append(list(map(int, dataArray)))
                    print(dataArray)
            else:
                p = int(data)


    return keys,p

if __name__ == '__main__':
    segredo = "eba"
    #
    # keys = generateKeysFromSecret(segredo)
    # keyStr = []
    # for key in keys:
    #     keyStr.append('-'.join(map(str,key)))
    #
    # contador = 0
    # for key in keyStr:
    #     contador +=1
    #     QrcodeManager.createQrcode(key,'keys/'+"key_"+str(contador) + '.png')
    #
    # qrCodes = os.listdir('keys')
    # for name in qrCodes:
    #     QrcodeManager.readQrcode("keys/"+name)