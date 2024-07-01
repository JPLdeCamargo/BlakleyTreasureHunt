import random

# Inherits MillerRobin in order to use _modular_power
class Fermat():

    # Simple Fermat implementation, 
    # only if the result from the modular exponentiation is not 1
    @staticmethod
    def exec(n, n_tests):
        if(n%2 == 0) : return False

        for i in range(n_tests):
            a = random.randint(2, n-2)
            mod_val = pow(a, n-1, n)
            if mod_val != 1:
                return False

        return True

    # wrapper used in testing, fixed n_tests to 50
    def wrapper(self, n):
        return self.exec(n, 50)
