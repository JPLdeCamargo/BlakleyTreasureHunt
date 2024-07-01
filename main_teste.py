from blakley import Blakley


message = "joao"
message_bytes = message.encode("utf-8")

print(memoryview(message_bytes).tolist())
for b in message_bytes:
    print(b)

d = int.from_bytes(message_bytes)
print(d)
print(message_bytes.decode("utf-8"))

p = 686678994773402271601694088239
x0 = d
a = 2
b = 2
w = Blakley.encode(a, b, p, x0)
print(w)
subset_w = w[:b+1]
decoded = Blakley.decode(subset_w, p)
print(decoded)
algo = bin(decoded)

bin_string = algo
binary_int = int(bin_string, 2)
byte_number = binary_int.bit_length() + 7 // 8
binary_array = binary_int.to_bytes(byte_number, "big")
print(binary_array.decode())