# Ejercicio 9
# Dada una frase introducida por teclado, guarda en un conjunto todas las palabras que acaben por la letra
# indicada por el usuario.

s = input("Frase: ")
letter = input("Letra: ")

s = s.lower()
letter = letter.lower()
words = s.split(" ")
ends_with = set()

for w in words:
    if w.endswith(letter):
        ends_with.add(w)

print(ends_with)


