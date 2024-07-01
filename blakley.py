import numpy as np
from sympy import Matrix

import random

class Blakley:

    # TODO: change data from int to byte array
    @staticmethod
    def encode(a:int, b:int, p:int, data:int) :
        v = [data]
        for i in range(b):
            v.append(random.randint(0, p-1))
        n = a+b+1
        ws = []
        for i in range(n):
            w = [random.randint(0, p-1) for j in range(b)]
            wv_sum = 0
            for j in range(b):
                wv_sum += w[j]*v[j]
            c = (v[b] - wv_sum) % p
            w.append(c)
            ws.append(w)
        return ws

    @staticmethod
    def decode(w, p:int):
        cs = []
        for i in range(len(w)):
            cs.append(-1*w[i][-1])
            w[i][-1] = -1
        w = Matrix(w)
        cs = np.array(cs)
        try:
            inverted_mod = w.inv_mod(p)
        except Exception as e:
            print(e)
            print("Inverted matrix can't be calculated")
        secret, _, _ = np.dot(inverted_mod, cs) % p
        return secret

if __name__ == "__main__":
    p = 686678994773402271601694088239
    x0 = 42
    a = 2
    b = 2
    w = Blakley.encode(a, b, p, x0)
    subset_w = w[:b+1]
    decoded = Blakley.decode(subset_w, p)
    print(decoded)


