from Blakley import Blakley
from Fermat import Fermat
from QRHandler import QRHandler

class TreasureHuntController:
    @staticmethod
    def create_new_hunt(num_keys:int, num_required:int, secret:str) -> bool:
        secret_bytes = secret.encode("utf-8")
        secret_int = int.from_bytes(secret_bytes)
        p = TreasureHuntController.__get_large_enough_prime(secret_int)
        b = num_required - 1
        a = num_keys - b - 1
        blakley = Blakley(a, b, p)
        keys = blakley.encode(secret_int)
        QRHandler.generateQrCodesFromSecret(keys, p)
        
    @staticmethod  
    def __get_large_enough_prime(num:int):
        num += 1
        if num % 2 == 0: num += 1
        while Fermat.exec(num, 50) == False:
            num += 2
        return num

    @staticmethod
    def get_treasure(keys_file_path:list[str], prime_file_path:list[str]) -> str:
        keys = []
        for key_path in keys_file_path:
            data = QRHandler.read_qr(key_path)
            if data is None:
                print("Error while reading qrcode")
                return
            data_array = data.split('-')
            keys.append(list(map(int, data_array)))

        prime_data = QRHandler.read_qr(prime_file_path)
        prime = int(prime_data)

        b = len(keys[0]) - 1
        if(b+1 > len(keys_file_path)):
            print("Not enough keys")
            return

        blakley = Blakley(0, b, prime)
        secret_num = blakley.decode(keys[:b+1])
        treasure = TreasureHuntController.__convert_int_to_utf8(secret_num)
        return treasure

    @staticmethod 
    def __convert_int_to_utf8(num ):
        bin_string = bin(num)
        binary_int = int(bin_string, 2)
        byte_number = binary_int.bit_length() + 7 // 8
        binary_array = binary_int.to_bytes(byte_number, "big")
        return binary_array.decode()





