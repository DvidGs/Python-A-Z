# Ejercicio 8
# Crea una función que dado un color en hexadecimal devuelva una lista de 3 posiciones, cada una de ellas
# correspondiente al valor R, G o B en este orden. Los valores de RGB varían entre 0 y 255.

def hex_to_decimal(hex_num):
    """
    Dado un número dexadecimal en formato string lo transforma a número decimal.
    Args:
        hex_num: String
    Returns:
        dec: Número entero
    """
    hex_to_dec = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                  "8": 8, "9": 9, "A": 10, "B": 11, "C":12, "D": 13, "E": 15, "F": 15}

    dec = 0
    for i in range(len(hex_num)):
        dec += hex_to_dec[hex_num[i]] * 16 ** (len(hex_num) - (i + 1))

    return dec

def hex_color_to_rgb(color_hex):
    """Dado un color en forma hexadecimal lo devuelve en forma de RGB
    Args:
        color_hex: String de 6 caracteres
    Returns:
        rgb: Lista de tamaño 3
    """
    color_hex = color_hex.upper()
    if len(color_hex) == 6:
        r = color_hex[:2]
        r = hex_to_decimal(r)
        g = color_hex[2:4]
        g = hex_to_decimal(g)
        b = color_hex[4:]
        b = hex_to_decimal(b)

        return [r, g, b]

    else:
        print("Un color en forma hexadecimal consta de 6 caracteres")

        