# Ejercicio 10
# Dada una lista de palabras, ordénalos con sorted() por número de consonates de mayor a menor.

def total_consonants(w):
    """
    Devuelve el total de consonantes de una palabra
    :arg
    :param w: Palabra en formato string
    :return:
        consonants: Número entero
    """
    consonants = 0
    for c in w:
        if c not in ["a", "e", "i", "o", "u"]:
            consonants += 1
    return consonants

words = ["david", "gallego", "python", "hi"]
print(sorted(words, key=total_consonants, reverse=True))

