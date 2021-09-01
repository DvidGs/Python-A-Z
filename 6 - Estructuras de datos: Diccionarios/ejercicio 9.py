# Ejercicio 9
# Crea un programa que pida el número de palabras a introducir. Crear un diccionario de clave la palabra y
# de valor el número de vocales de la palabra.

numero = int(input("¿cuántas palabras va a introducir? "))
palabras= {}
contador = 0

for i in range(numero):
    palabra = input("palabra: ")
    for v in palabra:
        if v == "a" or v == "e" or v == "i" or v == "o" or v == "u":
            contador += 1
    palabras[palabra] = contador
    print(palabras)
