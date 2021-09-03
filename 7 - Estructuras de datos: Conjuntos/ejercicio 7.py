# Ejercicio 7
# Dada una frase introducida por teclado, guarda en un conjunto la primera letra de cada palabra sin hacer
# uso del método .split().

frase = input("Frase: ")
primera_letra = set()

for i in frase.title():
    if i.isupper():
        primera_letra.add(i.lower())

print(primera_letra)