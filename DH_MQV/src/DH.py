from random import randint


class DH:
    def __init__(self, min_x=1000, max_x=10000):
        self.min_x = min_x
        self.max_x = max_x

    def get_x(self):
        return randint(self.min_x, self.max_x)

    def get_X(self, x, n, g):
        X = g ** x % n
        return X

    def get_k(self, Y, x, n):
        k = Y ** x % n
        return k
