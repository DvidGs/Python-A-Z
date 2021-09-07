# Ejercicio 3
# Dada una frase proporcionada por el usuario, crea una lista de tuplas indicando palabra, longitud de cada
# palabra, letra inicial y posición que ocupan dentro de la frase.

s = input()
s = s.lower()
words = s.split(" ")
info = []

for i in range(len(words)):
    info.append((words[i], len(words[i]), words[i][0], i))

print(info)
