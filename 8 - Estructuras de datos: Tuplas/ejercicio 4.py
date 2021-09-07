# Ejercicio 4
# Haz que el usuario introduzca palabras hasta que introduzca una palabra vacía. Guarda todas las palabras
# en una tupla y muestra la primera y la última introducidas haciendo uso del método unpacking.
# PISTA: Para guardar los elementos de uno en uno vas a tener que utilizar un tipo de dato que no es tupla
# y luego transformarlo a tupla.

w = input()
words = []

while w != "":
    words.append(w)
    w = input()
words = tuple(words)

first, *_, last = words
print("Primera palabra:", first)
print("Ultima palabra", last)

