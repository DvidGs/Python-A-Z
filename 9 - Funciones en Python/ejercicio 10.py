# Ejercicio 10
# Crea una función que dado un string por parámetro cuente cuántas veces sale cada caracter en dicho string
# y devuelva toda esa información en un diccionario.

def count_characters(s):
    """Dado un string, devuelve un diccionario con el número de apariciones
    de cada caracter del string.
    Args:
        s: String
    Returns:
        info: Diccionario
    """
    s = s.lower()
    info = {}
    for c in s:
        if c == " ":
            if "black" not in info.keys():
                info["black"] = s.count(c)
            elif c not in info.keys():
                info[c] = s.count(c)
            return info

