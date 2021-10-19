# Ejercicio 3
# Dada una lista de palabras, quédate con filter() con las que tengan más vocales que consonantes. Nece-
# sitarás una función que devuelva si una palabra tiene más vocales que consonantes.

def more_vowels(w):
    """
    Devuelve si hay más vocales que consonantes en una palabra
    :param w: Palabra en formato string
    :return:  Booleano
    """
    consonants = 0
    vowels = 0
    for c in w.lower():
        if c in ["a", "e", "i", "o", "u"]:
            vowels += 1
        else:
            consonants += 1
    return vowels > consonants

words = ["gallego", "aeio", "david", "python"]
print(list(filter(more_vowels, words)))



