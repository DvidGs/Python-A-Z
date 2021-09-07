# Ejercicio 6
# Haz que el usuario introduzca palabras hasta que introduzca una palabra vacía. Guarda todas las palabras
# en una tupla y muestra la tupla y el número total de caracteres que ha introducido.
# PISTA: Para guardar los elementos de uno en uno vas a tener que utilizar un tipo de dato que no es tupla
# y luego transformarlo a tupla.

w =input()
words = []

while w != "":
    words.append(w)
    w = input()

words = tuple(words)
total_chrs = 0

for w in words:
    total_chrs += len(w)

print("Tus palabras han sido {} y suman {} caracteres".format(words, total_chrs))
