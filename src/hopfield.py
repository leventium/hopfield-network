from typing import Callable
import numpy as np
from convert import Convert

class HopfieldNetwork:
    def __init__(
            self,
            matrix_width: int,
            detection_epochs: int,
            activation: Callable
        ) -> None:
        self.matrix_width = matrix_width
        self.detection_epochs = detection_epochs
        self.activation_func = activation
        self.matrix = np.zeros((matrix_width ** 2, matrix_width ** 2))

    def _activate_vector(self, vec: np.ndarray) -> np.ndarray:
        res = np.zeros((vec.size, ))
        for i in range(vec.size):
            res[i] = self.activation_func(vec[i])
        return res


    def fit(self, elems: list[np.ndarray]) -> None:
        for img in elems:
            self.matrix += np.matmul(
                img.reshape(self.matrix_width ** 2, 1),
                img.reshape(1, self.matrix_width ** 2)
            )
        for i in range(self.matrix_width):
            self.matrix[i][i] = 0

    def detect(self, elem: np.ndarray):
        first_round = True
        prev = elem.reshape(self.matrix_width ** 2, 1)
        curr = None

        for _ in range(self.detection_epochs):
            mul_result = np.matmul(self.matrix, prev)
            curr = self._activate_vector(mul_result)
            if first_round:
                first_round = False
                prev = curr
                continue
            if (prev == curr).all():
                return curr
            prev = curr
        return curr
