from src.DH import DH


class MQV(DH):
    def get_k_mqv(self, Y, x, a, A, B, n):
        k = (B * Y ** B) ** (a + x * A) % n
        return k
