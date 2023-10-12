from hopfield import HopfieldNetwork
from convert import Convert
import symbols.symbols_14x14 as s


def main():
    h = HopfieldNetwork(
        matrix_width=14,
        detection_epochs=20
    )
    h.fit([Convert.encode(elem) for elem in [
        s.K, s.E, s.L, s.R, s.F, s.V, s.M, s.I
    ]])

    for predict in [s.K_, s.E_, s.L_]:
        print(Convert.decode(14, Convert.encode(predict)), "\n\n")
        print(Convert.decode(14, h.detect(Convert.encode(predict))))
        print("\n\n--------------------------\n\n")


if __name__ == "__main__":
    main()
