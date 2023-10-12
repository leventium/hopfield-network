from hopfield import HopfieldNetwork
from convert import Convert
import symbols.symbols as s


def main():
    h = HopfieldNetwork(
        matrix_width=12,
        detection_epochs=20,
        activation=lambda x: 1 if x >= 0 else 0
    )
    h.fit([Convert.encode(elem) for elem in [
        s.K, s.R, s.E, s.V, s.F, s.M, s.I, s.L
    ]])
    print(Convert.decode(h.detect(Convert.encode(s.F))))


if __name__ == "__main__":
    main()
