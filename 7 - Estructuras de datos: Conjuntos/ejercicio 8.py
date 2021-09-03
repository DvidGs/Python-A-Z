# Ejercicio 8
# Dada una frase introducida por teclado, guarda en un conjunto todas las palabras con longitud par.

frase = input("Frase: ")
frase = frase.lower()

palabras = frase.split(" ")
conjunto_palabras = set()

for i in palabras:
    if len(i) % 2 == 0:
        conjunto_palabras.add(i)

print(conjunto_palabras)
