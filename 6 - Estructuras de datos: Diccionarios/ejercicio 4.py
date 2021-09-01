# Ejercicio 4
# Crea un programa que lea números enteros hasta que introduzca el 0 y devuelva un diccionario con la
# cantidad números positivos y negativos introducidos.

n = int(input("Número entero: "))
pos = 0
total = 0

while n != 0:
    if n > 0:
        pos += 1
    total += 1
    n = int(input("Número entero: "))

nums = {"positive": pos, "negative": total - pos}
print(nums)

