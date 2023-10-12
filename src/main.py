from hopfield import HopfieldNetwork
from convert import Convert
import symbols.symbols_14x14 as s


def main():
    h = HopfieldNetwork(
        matrix_width=14,
        detection_epochs=20,
        activation=lambda x: 1 if x >= 0 else 0
    )
    h.fit([Convert.encode(elem) for elem in [
        s.K, s.E, s.L
    ]])
    print(Convert.decode(14, h.detect(Convert.encode(s.K_))))


if __name__ == "__main__":
    main()
