# Ejercicio 8
# Crea un programa que pida el número de palabras a introducir. Crear un diccionario de clave la palabra y
# de valor la longitud de dicha palabra.

numero = int(input("¿número de palabras?"))
palabras = {}

for i in range(numero):
    palabra = input("palabra: ")
    palabras[palabra] = len(palabra)

print(palabras)
