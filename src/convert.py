import numpy as np


class Convert:
    @staticmethod
    def encode(symbol: str) -> np.ndarray:
        res = np.zeros((len(symbol), ), dtype=int)
        for i, c in enumerate(symbol):
            res[i] = 1 if c == "#" else -1
        return res

    @staticmethod
    def decode(width: int, arr) -> str:
        res = ""
        for m in range(width):
            for i in range(width):
                res += "#" if arr[width*m+i] == 1 else " "
            res += "\n"
        return res
