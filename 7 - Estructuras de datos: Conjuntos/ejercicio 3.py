# Ejercicio 3
# Dada una frase introducida por teclado, guarda en un conjunto todas las palabras que empiecen por la letra
# indicada por el usuario.

frase = input("Frase: ")
letra = input("Letra: ")

frase = frase.lower()
letra = letra.lower()
palabras = frase.split(" ")
starts_with = set()

for i in palabras:
    if i.startswith(letra):
        starts_with.add(i)
print(starts_with)