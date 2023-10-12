import cv2
from hopfield import HopfieldNetwork
from convert import Convert
import symbols.symbols_14x14 as s
import numpy as np

RESIZE_TO = 100

def change(w, arr):
    res = np.zeros((w, w), dtype=int)
    for i in range(w):
        for j in range(w):
            res[i][j] = 1 if arr[i][j] == 1 else -1
    return res

def main():
    h = HopfieldNetwork(
        matrix_width=RESIZE_TO,
        detection_epochs=20,
        activation=lambda x: 1 if x >= 0 else 0
    )
    for elem in [s.K, s.R, s.E, s.V, s.M, s.I, s.L, s.F]:
        im = change(RESIZE_TO, cv2.resize(
            Convert.encode_matrix(14, elem),
            (RESIZE_TO, RESIZE_TO),
            interpolation=cv2.INTER_NEAREST
        ))
        print(Convert.decode(RESIZE_TO, np.concatenate(im.reshape(1, RESIZE_TO * RESIZE_TO))))
        h.fit([im])
    print(Convert.decode(
        RESIZE_TO,
        h.detect(
            cv2.resize(
                Convert.encode_matrix(14, s.L_),
                (RESIZE_TO, RESIZE_TO),
                interpolation=cv2.INTER_NEAREST
            )
        )
    ))


if __name__ == "__main__":
    main()
