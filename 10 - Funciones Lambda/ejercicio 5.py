# Ejercicio 5
# Dada una lista de palabras, quédate con reduce() con la palabra más larga. Necesitarás una función que
# compare dos palabras y devuelva la que tenga mayor longitud.

from functools import reduce

def longer_word(w1, w2):
    """
    Devuelve la palabra de mayor longitud
    :args:
    :param w1: Palabra en formato string
    :param w2: Palabra en formato string
    :return: Palabra en formato string
    """

    if len(w1) >= len(w2):
        return w1
    return w2

words = ["david", "gallego", "python"]
print(reduce(longer_word, words))


