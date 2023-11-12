import symbols.symbols_10x10 as s

with open("data.hex", "w") as file:
    for sym in (s.K, s.R, s.E, s.V, s.F, s.M, s.I, s.L, s.R):
        for c in sym:
            file.write("0001" if c == "#" else "ffff")
        file.write("\n")
