import numpy as np


class Convert:
    @staticmethod
    def encode(symbol: str) -> np.ndarray:
        res = np.zeros((len(symbol), ), dtype=int)
        for i, c in enumerate(symbol):
            res[i] = 1 if c == "#" else -1
        return res

    @staticmethod
    def decode(arr) -> str:
        res = ""
        for m in range(12):
            for i in range(12):
                res += "#" if arr[12*m+i] == 1 else " "
            res += "\n"
        return res
