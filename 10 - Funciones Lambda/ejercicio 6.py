# Ejercicio 6
# Dada una lista de palabras, calcula el número de vocales de cada una con map().

def total_vowels(w):
    """
    Devuelve el total de vocales de una palabra
    :arg
    :param w: palabra en formato strinng
    :return:
        :cosonants: Número entero
    """
    vowels = 0
    for c in w:
        if c in ["a", "e", "i", "o", "u"]:
            vowels += 1
    return vowels

words = ["david", "gallego", "python"]
print(list(map(lambda w: total_vowels(w), words)))



