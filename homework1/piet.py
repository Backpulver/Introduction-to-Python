# Piet
def calculate_final_vector(coords, hexes):
    x1 = coords[0]
    y1 = coords[1]
    for hex in hexes:
        hex = hex.lower()
        if hex == "ffffff":
            continue
        elif hex == "000000":
            break
        elif hex == "c0ffc0" or hex == "c00000":
            x1 -= 1
        elif hex == "00c000" or hex == "ffc0c0":
            x1 += 1
        elif hex == "c0c000" or hex == "c0c0ff":
            y1 += 1
        elif hex == "ffffc0" or hex == "0000c0":
            y1 -= 1
        else:
            print("I should not be here")
    return (x1, y1)
