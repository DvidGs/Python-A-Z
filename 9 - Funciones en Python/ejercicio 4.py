# Ejercicio 4
# Crea una función que devuelva True si el caracter introducido por parámetro se trata de una vocal y False
# en caso contrario.

def is_vowel(c):
    """
    Devuelve si el caracter dado es una vocal.
    Args:
        c: Caracter
    Returns:
        Booleano
    """
    if len(c) == 1:
        if c.lower() in ["a", "e", "i", "o", "u"]:
            return True
        return False
    else:
        print("Solo se debe ingresar un caracter")

print(is_vowel("e"))
