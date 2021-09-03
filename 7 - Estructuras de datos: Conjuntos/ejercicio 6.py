# Ejercicio 6
# Dada una frase introducida por teclado, guarda en un conjunto todas las palabras que contengan la letra
# indicada por el usuario.

frase = input("Frase: ")
letra = input("Letra: ")

frase = frase.lower()
letra = letra.lower()
palabras = frase.split(" ")
baul_letra = set()

for i in palabras:
    if letra in i:
        baul_letra.add(i)

print(baul_letra)
