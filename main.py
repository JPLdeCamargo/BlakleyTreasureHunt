from TreasureHuntController import TreasureHuntController


if __name__ == "__main__":
    secret_file = open("segredo.txt")
    secret = secret_file.read()
    hunt_controller = TreasureHuntController.create_new_hunt(5, 3, secret)
    key_paths = ["keys/normal/key_" + str(i+1) + ".png" for i in range(5)]
    prime_path = "keys/normal/prime.png"

    print(TreasureHuntController.get_treasure(key_paths, prime_path))