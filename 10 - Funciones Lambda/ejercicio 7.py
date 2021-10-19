# Ejercicio 7
# Dada una lista de palabras, quédate con reduce() y map() con la palabra con más consonantes. Necesitarás
# una función que cuente el número de consonantes de una palabra y otra que dados dos números, devuelva el
# mayor.

from functools import reduce

def total_consonants(w):
    """
    devuelve el total de consonantes de una palabra
    :arg
    :param w: palabra en formato string
    :return:
        consonants: Número entero
    """
    consonants = 0
    for c in w:
        if c not in ["a", "e", "i", "o", "u"]:
            consonants += 1
        return consonants

def bigger_than(a, b):
    """
    Devuelve el máximo entre dos numeros
    :arg:
    :param a: Número real
    :param b: Número real
    :return:
        Número real
    """
    if a > b:
        return a
    return b

words = ["david", "gallego", "python", "hi"]
print(words)
num_consonants = list(map(lambda w: total_consonants(w), words))
print(num_consonants)
reduce(bigger_than, num_consonants)



