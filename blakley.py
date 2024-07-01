import numpy as np
from sympy import Matrix

import random

class Blakley:

    def __init__(self, a, b, p):
        self.a: int = a
        self.b: int = b
        self.p: int = p

    def encode(self, data: int):
        v = [data]
        for i in range(self.b):
            v.append(random.randint(0, self.p-1))
        n = self.a + self.b + 1
        ws = []
        for i in range(n):
            w = [random.randint(0, self.p-1) for j in range(self.b)]
            wv_sum = 0
            for j in range(self.b):
                wv_sum += w[j]*v[j]
            c = (v[self.b] - wv_sum) % self.p
            w.append(c)
            ws.append(w)
        return ws

    def decode(self,w):
        cs = []
        for i in range(len(w)):
            cs.append(-1*w[i][-1])
            w[i][-1] = -1
        w = Matrix(w)
        cs = np.array(cs)
        try:
            inverted_mod = w.inv_mod(self.p)
        except Exception as e:
            print(e)
            print("Inverted matrix can't be calculated")
        secret, _, _ = np.dot(inverted_mod, cs) % self.p
        return secret

if __name__ == "__main__":
    p = 686678994773402271601694088239
    x0 = 42
    a = 2
    b = 2
    blakley = Blakley(a,b,p)
    w = blakley.encode(x0)
    subset_w = w[:b+1]
    decoded = blakley.decode(subset_w)
    print(decoded)


