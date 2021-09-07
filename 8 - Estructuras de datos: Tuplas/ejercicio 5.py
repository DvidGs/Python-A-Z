# Ejercicio 5
# Dada una lista de palabras, crea otra lista del mismo tamaño que guarde la longitud de cada palabra. Usa
# la función zip() para crear un diccionario con claves las palabras y valores, su longitud.

words = ["ola", "caracola", "piña", "plata"]
words_len = []

for w in words:
    words_len.append(len(w))

print(dict(zip(words, words_len)))

